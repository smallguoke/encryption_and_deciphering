import hashlib


class Sha1_a:
    data = ""

    def __init__(self):
        pass

    def encrypt(self):
        sha1 = hashlib.sha1()
        sha1.update(self.data.encode('utf-8'))
        sha1_data = sha1.hexdigest()
        return sha1_data


