# Custom expanded version of SHA512
import hashlib


class PMHash:
    digest_size = 256
    name = 'PMHash'

    def __init__(self, b=b""):
        self.b = b

    def update(self, b):
        self.b += b

    def digest(self):
        return hashlib.sha512(
                self.b + b'\0'
            ).digest() + hashlib.sha512(
                self.b + b'\1'
            ).digest() + hashlib.sha512(
                self.b + b'\2'
            ).digest() + hashlib.sha512(
                self.b + b'\3'
            ).digest()

    def hexdigest(self):
        return self.digest().hex()

    def copy(self):
        return PMHash(self.b)


def pmhash(b=b""):
    return PMHash(b)
