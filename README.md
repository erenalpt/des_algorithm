# des_algorithm

DES (Data Encryption Standard)

DES is a standard developed to encrypt data and open encrypted data. The algorithm mainly used is called DEA, namely Data Encryption Algorithm. The standardized version of this algorithm is called DES.

DES is a block cipher, and encrypts data in blocks of size of 64 bit each, means 64 bits of plain text goes as the input to DES, which produces 64 bits of cipher text. The same algorithm and key are used for encryption and decryption, with minor differences. The key length is 56 bits. The basic idea is show in figure.

I will use https://pypi.org/project/des/. I demonstrated the use in a simple way. Available in code. I did not delete the byte-b statement in print method. I know it doesn't look nice. But I thought he had to stop there to see where he was coming from. 
