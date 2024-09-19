alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.index("a")
cool = "IDK MAN WHAT DO U WANT"

def encrypt(x, a, c):
    return (x * a + c) % len(alphabet)

def encrypt_text(txt):
    for char in txt:
        index = encrypt(alphabet.index(char), 5, 2)
        newChar = alphabet[index]
        array.append(newChar)

    return "".join(array)

def decrypt(x, a, c):
    return 

print(encrypt_text(cool))