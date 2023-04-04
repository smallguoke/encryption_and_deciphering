import base64
from Crypto.Cipher import AES


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


class Aes_a:
    def __init__(self):
        pass

    # 加密方法
    def encrypt(self,key, text):
        aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
        encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
        return encrypted_text


    # 解密方法
    def decrypt(self,key, miwen):
        aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
        base64_decrypted = base64.decodebytes(miwen.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
        return decrypted_text


if __name__ == '__main__':
    data = '123456'
    key = '123456'
    sss = Aes_a()
    miwen = sss.encrypt(key, data)
    print(miwen)
    mingwen = sss.decrypt(key, miwen)
    print(mingwen)
