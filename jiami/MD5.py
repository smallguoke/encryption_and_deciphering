import hashlib


class Md5_a:
    data = ''

    def __init__(self):
        pass

    def encrypt(self):
        m = hashlib.md5(self.data.encode("utf-8"))
        md5 = m.hexdigest()
        return md5
