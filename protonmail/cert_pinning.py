import base64
import hashlib
from ssl import DER_cert_to_PEM_cert

from OpenSSL import crypto
from requests.adapters import HTTPAdapter
from urllib3.connectionpool import HTTPSConnectionPool
from urllib3.poolmanager import PoolManager
from urllib3.util.timeout import Timeout
from .exceptions import TLSPinningError
from .constants import PUBKEY_HASH_DICT


class TLSPinningHTTPSConnectionPool(HTTPSConnectionPool):
    """Verify the certificate upon each connection"""
    def __init__(
        self,
        host,
        hash_dict,
        port=None,
        strict=False,
        timeout=Timeout.DEFAULT_TIMEOUT,
        maxsize=1,
        block=False,
        headers=None,
        retries=None,
        _proxy=None,
        _proxy_headers=None,
        key_file=None,
        cert_file=None,
        cert_reqs=None,
        key_password=None,
        ca_certs=None,
        ssl_version=None,
        assert_hostname=None,
        assert_fingerprint=None,
        ca_cert_dir=None,
        **conn_kw
    ):
        self.hash_dict = hash_dict
        # try/except is needed for multi-version compatibility,
        # as number of args chane from version 16/18 to 20.
        try:
            super(TLSPinningHTTPSConnectionPool, self).__init__(
                host,
                port,
                strict,
                timeout,
                maxsize,
                block,
                headers,
                retries,
                _proxy,
                _proxy_headers,
                key_file,
                cert_file,
                cert_reqs,
                key_password,
                ca_certs,
                ssl_version,
                assert_hostname,
                assert_fingerprint,
                ca_cert_dir,
                **conn_kw
            )
        except TypeError:
            super(TLSPinningHTTPSConnectionPool, self).__init__(
                host,
                port,
                strict,
                timeout,
                maxsize,
                block,
                headers,
                retries,
                _proxy,
                _proxy_headers,
                key_file,
                cert_file,
                cert_reqs,
                ca_certs,
                ssl_version,
                assert_hostname,
                assert_fingerprint,
                ca_cert_dir,
                **conn_kw
            )

    def _validate_conn(self, conn):
        super(TLSPinningHTTPSConnectionPool, self)._validate_conn(conn)
        pem_certificate = self.__get_certificate(conn.sock)
        self.ensure_session_is_secure(pem_certificate, conn)

    def ensure_session_is_secure(self, cert, conn):
        """Check if connection is secure"""

        cert_hash = self.__extract_hash(cert)

        if not self.__is_hash_valid(cert_hash):
            # Also generate a report
            conn.close()
            raise TLSPinningError("Insecure connection")

    def __extract_hash(self, cert):
        """Extract encrypted hash from the certificate."""
        cert_obj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        pubkey_obj = cert_obj.get_pubkey()
        pubkey = crypto.dump_publickey(crypto.FILETYPE_ASN1, pubkey_obj)

        spki_hash = hashlib.sha256(pubkey).digest()
        cert_hash = base64.b64encode(spki_hash).decode('utf-8')
        return cert_hash

    def __is_hash_valid(self, cert_hash):
        """Validate the hash against a known list of hashes/pins.

        Returns:
            bool: False if hash is not valid
                  True if hash is valid
        """
        # host is passed in __init__
        try:
            self.hash_dict[self.host].index(cert_hash)
        except (ValueError, KeyError, TypeError):
            pass
        else:
            return True

        # try alt routing
        try:
            self.hash_dict["backup"].index(cert_hash)
        except (ValueError, KeyError, TypeError):
            return False
        else:
            return True

    def __get_certificate(self, sock):
        """Extract and convert certificate to PEM format"""
        certificate_binary_form = sock.getpeercert(True)
        return DER_cert_to_PEM_cert(certificate_binary_form)


class TLSPinningPoolManager(PoolManager):
    """Attach TLSPinningHTTPSConnectionPool to TLSPinningPoolManager"""
    def __init__(
        self,
        hash_dict,
        num_pools=10,
        headers=None,
        **connection_pool_kw
    ):
        self.hash_dict = hash_dict
        super(TLSPinningPoolManager, self).__init__(
            num_pools=10, headers=headers, **connection_pool_kw
        )

    def _new_pool(self, scheme, host, port, request_context):
        if scheme != 'https':
            return super(TLSPinningPoolManager, self)._new_pool(
                scheme, host, port, request_context
            )

        return TLSPinningHTTPSConnectionPool(
            host=host, port=port,
            hash_dict=self.hash_dict, **self.connection_pool_kw
        )


class TLSPinningAdapter(HTTPAdapter):
    """Attach TLSPinningPoolManager to TLSPinningAdapter"""
    def __init__(self, hash_dict=PUBKEY_HASH_DICT):
        self.hash_dict = hash_dict
        super(TLSPinningAdapter, self).__init__()

    def init_poolmanager(
        self,
        connections,
        maxsize,
        block=False,
        **pool_kwargs
    ):
        self.poolmanager = TLSPinningPoolManager(
            num_pools=connections, maxsize=maxsize, block=block,
            strict=True, hash_dict=self.hash_dict, **pool_kwargs
        )
