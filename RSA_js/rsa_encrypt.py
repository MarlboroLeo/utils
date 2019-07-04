# coding=utf-8
# @Time    : 2019/6/19 9:17
# @Author  : Leau
# @File    : rsa_encrypt.py
import rsa


class Encrypt(object):
    def __init__(self, e, m):
        self.e = e
        self.m = m

    def encrypt(self, message):
        mm = int(self.m, 16)
        ee = int(self.e, 16)
        rsa_pubkey = rsa.PublicKey(mm, ee)
        crypto = self._encrypt(message.encode(), rsa_pubkey)
        return crypto.hex()

    def _pad_for_encryption(self, message, target_length):
        message = message[::-1]
        # max_msglength = target_length - 11
        msglength = len(message)

        padding = b''
        padding_length = target_length - msglength - 3

        for i in range(padding_length):
            padding += b'\x00'

        return b''.join([b'\x00\x00', padding, b'\x00', message])

    def _encrypt(self, message, pub_key):
        keylength = rsa.common.byte_size(pub_key.n)
        padded = self._pad_for_encryption(message, keylength)

        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
        block = rsa.transform.int2bytes(encrypted, keylength)

        return block


def encrypt(e, m, message):
    en = Encrypt(e, m)
    return en.encrypt(message)


if __name__ == '__main__':
    exponent = '10001'
    modulus = '00822d7485ebf31ea1acb3840c113c02dfe7cbedc9539e2fd6cc6cb0e38c5675fa42807cb901ad1ba912caf9cb3a8381c81249ac46d7bab96fe9d53caaf036681d91601f080073b277ef8e2b972b8a289683c9959f5fe63fc35f4438c0c469f5a732262edc786addc088892f5ef538b775b5f8a88d6b9f01f349d3309284361fc1'
    print(encrypt(exponent, modulus, 'PDAA201711010000502986'))
