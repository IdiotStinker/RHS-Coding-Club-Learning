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

def decrypt_text(text):
    array = []
    for char in text:
        index = decrypt(alphabet.index(char), 5, 2)
        newChar = alphabet[index]
        array.append(newChar)

    return "".join(array)

def find_inverse(a):
    for i in range(1, len(alphabet)):
        if (i * a) % len(alphabet) == 1:
            return i
    return -1

def decrypt(x, a, c):

    x += (len(alphabet) - c) % len(alphabet)
    inverse = find_inverse(a)

    x *= inverse
    x %= len(alphabet)

    return x

print(encrypt_text(plaintext))
print(decrypt_text(encrypt_text(plaintext)))