import random
chars = [chr(i) for i in range(33, 127)]
def vernam(orig, k):
    orig = [bin(ord(i))[2:].zfill(8) for i in orig]
    k = [bin(ord(i))[2:].zfill(8) for i in k]
    return "".join([chr(int(orig[i], 2) ^ int(k[i], 2)) for i in range(len(orig))])


while True:
    toEnc = input("Please enter the string to be encrypted: ")
    key = "".join([random.choice(chars) for i in toEnc])
    encrypted = vernam(toEnc, key)
    print(encrypted)
    decrypted = vernam(encrypted, key)
    print(decrypted + "\n")
