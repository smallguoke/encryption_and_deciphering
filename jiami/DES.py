import binascii
from pyDes import des, CBC, PAD_PKCS5


class Des_a:
    secret_key = ''
    s = ''
    data = ''
    key = ''

    def __init__(self):
        pass

    def des_encrypt(self):
        iv = self.secret_key
        k = des(self.secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(self.s, padmode=PAD_PKCS5)
        return binascii.b2a_hex(en)

    def des_decrypt(self):
        iv = self.key
        k = des(self.key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(self.data), padmode=PAD_PKCS5)
        return de


if __name__ == '__main__':
    sss = Des_a()
    sss.secret_key = '12345678'
    sss.s = '12345678'
    miw = sss.des_encrypt()
    # print(miw)
    miw = miw.decode('utf-8')
    # print(type(test_str))
    # bt = bytes(test_str,'utf-8')
    # print(type(bt))
    # # print(test_str)
    sss.key = '12345678'
    sss.data = miw
    print(sss.data)
    print(type(sss.data))
    print(sss.data)
    print(type(sss.key))
    print(sss.key)
    minw = sss.des_decrypt()
    print(minw.decode('utf-8'))



