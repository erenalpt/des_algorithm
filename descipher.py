# -*- coding: utf8 -*-

# https://github.com/0x10001/des
# The key should be of length 8, 16 or 24. The algorithm will be automatically chosen for you
# Note that the key should be written as bytes in Python 3.
# https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal

from des import DesKey

try:
    key_value = input("Please input 8-16-24 length text: ").encode()
    key0 = DesKey(key_value)  # Key 8-16-24 length

    enc_byte = input("Please enter text: ").encode()
    enc = key0.encrypt(enc_byte, padding=True)
    print("Encrypted text --> {0}".format(enc))

    print("Decrypted text --> {0}".format(key0.decrypt(enc, padding=True)))

except:
    print("Wrong usage. Please repeat running py script.")
