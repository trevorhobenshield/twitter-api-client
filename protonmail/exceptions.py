class ProtonError(Exception):
    def __init__(self, message, additional_context=None):
        self.message = message
        self.additional_context = additional_context
        super().__init__(self.message)


class NetworkError(ProtonError):
    """NetworkError"""


class TLSPinningError(ProtonError):
    """TLS Pinning exception"""


class ProtonAPIError(ProtonError):
    def __init__(self, ret):
        try:
            self.code = ret['Code']
            self.error = ret['Error']
        except: # noqa
            self.code = "N/A"
            self.error = "N/A"

        try:
            self.headers = ret["Headers"]
        except: # noqa
            self.headers = "N/A"

        super().__init__(self.error)


class NewConnectionError(ProtonError):
    """Network Error"""


class ConnectionTimeOutError(ProtonError):
    """Connection Time Out Error"""


class UnknownConnectionError(ProtonError):
    """UnknownConnectionError"""


class MissingDepedencyError(ProtonError):
    """Missing dependency error"""
