# N    A large safe prime (N = 2q+1, where q is prime)
#      All arithmetic is done modulo N.
# g    A generator modulo N
# k    Multiplier parameter (k = H(N, g) in SRP-6a, k = 3 for legacy SRP-6)
# s    User's salt
# I    Username
# p    Cleartext Password
# H()  One-way hash function
# ^    (Modular) Exponentiation
# u    Random scrambling parameter
# a,b  Secret ephemeral values
# A,B  Public ephemeral values
# x    Private key (derived from p and s)
# v    Password verifier

from __future__ import division

import ctypes
import sys, os

from .pmhash import pmhash
from .util import PM_VERSION, SRP_LEN_BYTES, SALT_LEN_BYTES, hash_password

dlls = list()

platform = sys.platform
if platform == 'darwin':
    dlls.append(ctypes.cdll.LoadLibrary('libssl.dylib'))
elif 'win' in platform:
    for d in ('libeay32.dll', 'libssl32.dll', 'ssleay32.dll'):
        try:
            dlls.append(ctypes.cdll.LoadLibrary(d))
        except Exception:
            pass
else:
    try:
        dlls.append(ctypes.cdll.LoadLibrary('libssl.so.10'))
    except OSError:
        try:
            dlls.append(ctypes.cdll.LoadLibrary('libssl.so.1.0.0'))
        except OSError:
            dlls.append(ctypes.cdll.LoadLibrary('libssl.so'))


class BIGNUM_Struct(ctypes.Structure):
    _fields_ = [("d", ctypes.c_void_p),
                ("top", ctypes.c_int),
                ("dmax", ctypes.c_int),
                ("neg", ctypes.c_int),
                ("flags", ctypes.c_int)]


class BN_CTX_Struct(ctypes.Structure):
    _fields_ = [("_", ctypes.c_byte)]


BIGNUM = ctypes.POINTER(BIGNUM_Struct)
BN_CTX = ctypes.POINTER(BN_CTX_Struct)


def load_func(name, args, returns=ctypes.c_int):
    d = sys.modules[__name__].__dict__
    f = None

    for dll in dlls:
        try:
            f = getattr(dll, name)
            f.argtypes = args
            f.restype = returns
            d[name] = f
            return
        except Exception:
            pass
    raise ImportError('Unable to load required functions from SSL dlls')


load_func('BN_new', [], BIGNUM)
load_func('BN_free', [BIGNUM], None)
load_func('BN_clear', [BIGNUM], None)
load_func('BN_set_flags', [BIGNUM, ctypes.c_int], None)

load_func('BN_CTX_new', [], BN_CTX)
load_func('BN_CTX_free', [BN_CTX], None)

load_func('BN_cmp', [BIGNUM, BIGNUM], ctypes.c_int)

load_func('BN_num_bits', [BIGNUM], ctypes.c_int)

load_func('BN_add', [BIGNUM, BIGNUM, BIGNUM])
load_func('BN_sub', [BIGNUM, BIGNUM, BIGNUM])
load_func('BN_mul', [BIGNUM, BIGNUM, BIGNUM, BN_CTX])
load_func('BN_div', [BIGNUM, BIGNUM, BIGNUM, BIGNUM, BN_CTX])
load_func('BN_mod_exp', [BIGNUM, BIGNUM, BIGNUM, BIGNUM, BN_CTX])

load_func('BN_rand', [BIGNUM, ctypes.c_int, ctypes.c_int, ctypes.c_int])

load_func('BN_bn2bin', [BIGNUM, ctypes.c_char_p])
load_func('BN_bin2bn', [ctypes.c_char_p, ctypes.c_int, BIGNUM], BIGNUM)

load_func('BN_hex2bn', [ctypes.POINTER(BIGNUM), ctypes.c_char_p])
load_func('BN_bn2hex', [BIGNUM], ctypes.c_char_p)

load_func('CRYPTO_free', [ctypes.c_char_p])

load_func('RAND_seed', [ctypes.c_char_p, ctypes.c_int])


def new_bn():
    bn = BN_new()
    BN_set_flags(bn, 0x04)  # BN_FLAG_CONSTTIME
    return bn


def bn_num_bytes(a):
    return ((BN_num_bits(a) + 7) // 8) # noqa


def bn_mod(rem, m, d, ctx):
    return BN_div(None, rem, m, d, ctx) # noqa


def bn_is_zero(n):
    return n[0].top == 0


def bn_to_bytes(n, num_bytes):
    b = ctypes.create_string_buffer(bn_num_bytes(n))
    BN_bn2bin(n, b) # noqa
    return b.raw[::-1].ljust(num_bytes, b'\0')


def bytes_to_bn(dest_bn, bytes):
    BN_bin2bn(bytes[::-1], len(bytes), dest_bn) # noqa


def bn_hash(hash_class, dest, n1, n2):
    h = hash_class()
    h.update(bn_to_bytes(n1, SRP_LEN_BYTES))
    h.update(bn_to_bytes(n2, SRP_LEN_BYTES))
    d = h.digest()
    bytes_to_bn(dest, d)


def bn_hash_k(hash_class, dest, g, N, width):
    h = hash_class()
    bin1 = ctypes.create_string_buffer(width)
    bin2 = ctypes.create_string_buffer(width)
    BN_bn2bin(g, bin1) # noqa
    BN_bn2bin(N, bin2) # noqa
    h.update(bin1)
    h.update(bin2[::-1])
    bytes_to_bn(dest, h.digest())


def calculate_x(hash_class, dest, salt, password, modulus, version):
    exp = hash_password(
        hash_class, password, salt, bn_to_bytes(modulus, SRP_LEN_BYTES), version
    )
    bytes_to_bn(dest, exp)


def update_hash(h, n):
    h.update(bn_to_bytes(n, SRP_LEN_BYTES))


def calculate_client_challenge(hash_class, A, B, K):
    h = hash_class()
    update_hash(h, A)
    update_hash(h, B)
    h.update(K)
    return h.digest()


def calculate_server_challenge(hash_class, A, M, K):
    h = hash_class()
    update_hash(h, A)
    h.update(M)
    h.update(K)
    return h.digest()


def get_ngk(hash_class, n_bin, g_hex, ctx):
    N = new_bn() # noqa
    g = new_bn() # noqa
    k = new_bn() # noqa

    bytes_to_bn(N, n_bin)
    BN_hex2bn(g, g_hex) # noqa
    bn_hash_k(hash_class, k, g, N, SRP_LEN_BYTES)

    return N, g, k


class User(object):
    def __init__(self, password, n_bin, g_hex=b"2", bytes_a=None, bytes_A=None): # noqa
        if bytes_a and len(bytes_a) != 32:
            raise ValueError("32 bytes required for bytes_a")

        if not isinstance(password, str) or len(password) == 0:
            raise ValueError("Invalid password")

        self.password = password.encode()
        self.a = new_bn() # noqa
        self.A = new_bn() # noqa
        self.B = new_bn() # noqa
        self.S = new_bn() # noqa
        self.u = new_bn() # noqa
        self.x = new_bn() # noqa
        self.v = new_bn() # noqa
        self.tmp1 = new_bn() # noqa
        self.tmp2 = new_bn() # noqa
        self.tmp3 = new_bn() # noqa
        self.ctx = BN_CTX_new() # noqa
        self.M = None
        self.K = None
        self.expected_server_proof = None
        self._authenticated = False
        self.bytes_s = None

        self.hash_class = pmhash
        self.N, self.g, self.k = get_ngk(self.hash_class, n_bin, g_hex, self.ctx) # noqa

        if bytes_a:
            bytes_to_bn(self.a, bytes_a)
        else:
            BN_rand(self.a, 256, 0, 0) # noqa

        if bytes_A:
            bytes_to_bn(self.A, bytes_A)
        else:
            BN_mod_exp(self.A, self.g, self.a, self.N, self.ctx) # noqa

    def __del__(self):
        if not hasattr(self, 'a'):
            return  # __init__ threw exception. no clean up required
        BN_free(self.a) # noqa
        BN_free(self.A) # noqa
        BN_free(self.B) # noqa
        BN_free(self.S) # noqa
        BN_free(self.u) # noqa
        BN_free(self.x) # noqa
        BN_free(self.v) # noqa
        BN_free(self.N) # noqa
        BN_free(self.g) # noqa
        BN_free(self.k) # noqa
        BN_free(self.tmp1) # noqa
        BN_free(self.tmp2) # noqa
        BN_free(self.tmp3) # noqa
        BN_CTX_free(self.ctx) # noqa

    def authenticated(self):
        return self._authenticated

    def get_ephemeral_secret(self):
        return bn_to_bytes(self.a, SRP_LEN_BYTES)

    def get_session_key(self):
        return self.K if self._authenticated else None

    def get_challenge(self):
        return bn_to_bytes(self.A, SRP_LEN_BYTES)

    # Returns M or None if SRP-6a safety check is violated
    def process_challenge(
        self, bytes_s, bytes_server_challenge, version=PM_VERSION
    ):
        self.bytes_s = bytes_s
        bytes_to_bn(self.B, bytes_server_challenge)

        # SRP-6a safety check
        if bn_is_zero(self.B):
            return None

        bn_hash(self.hash_class, self.u, self.A, self.B)

        # SRP-6a safety check
        if bn_is_zero(self.u):
            return None

        calculate_x(
            self.hash_class, self.x, self.bytes_s, self.password, self.N, version
        )
        BN_mod_exp(self.v, self.g, self.x, self.N, self.ctx)  # noqa

        # S = (B - k*(g^x)) ^ (a + ux)
        BN_mul(self.tmp1, self.u, self.x, self.ctx) # noqa
        BN_add(self.tmp2, self.a, self.tmp1) # noqa tmp2 = (a + ux)  
        BN_mod_exp(self.tmp1, self.g, self.x, self.N, self.ctx) # noqa
        BN_mul(self.tmp3, self.k, self.tmp1, self.ctx) # noqa tmp3 = k*(g^x)
        BN_sub(self.tmp1, self.B, self.tmp3)  # noqa tmp1 = (B - K*(g^x))
        BN_mod_exp(self.S, self.tmp1, self.tmp2, self.N, self.ctx) # noqa

        self.K = bn_to_bytes(self.S, SRP_LEN_BYTES)
        self.M = calculate_client_challenge(
            self.hash_class, self.A, self.B, self.K
        )
        self.expected_server_proof = calculate_server_challenge(
            self.hash_class, self.A, self.M, self.K
        )

        return self.M

    def verify_session(self, server_proof):
        if self.expected_server_proof == server_proof:
            self._authenticated = True

    def compute_v(self, bytes_s=None, version=PM_VERSION):
        if bytes_s is None:
            salt = new_bn()
            BN_rand(salt, 10*8, 0, 0) # noqa
            self.bytes_s = bn_to_bytes(salt, SALT_LEN_BYTES)
        else:
            self.bytes_s = bytes_s

        calculate_x(
            self.hash_class, self.x, self.bytes_s, self.password, self.N, version
        )
        BN_mod_exp(self.v, self.g, self.x, self.N, self.ctx)
        return self.bytes_s, bn_to_bytes(self.v, SRP_LEN_BYTES)

# ---------------------------------------------------------
# Init
#
RAND_seed(os.urandom(32), 32) # noqa
