alphabet = "abcdefghijklmnopqrstuvwxyz"
plaintext = "hello"

def encrypt(x, a, c):
    return (a * x + c) % (len(alphabet))

def encrypt_text(text):
    array = []
    for char in text:
        index = encrypt(alphabet.index(char), 5, 2)
        newChar = alphabet[index]
        array.append(newChar)

    return "".join(array)

def decrypt(x, a, c):
    return 

print(encrypt_text(plaintext))