import hmac
import hashlib


class Hmac:
    data = ''
    key = ''

    def __init__(self):
        pass

    def encrypt(self):
        data = bytes(self.data.encode('utf-8'))
        key = bytes(self.key.encode('utf-8'))
        mac = hmac.new(key, data, hashlib.md5)
        mac.digest()
        HMAC = mac.hexdigest()
        return HMAC
