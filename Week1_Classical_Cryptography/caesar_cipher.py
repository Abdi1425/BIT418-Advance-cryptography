def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = "HELLO WORLD"

encrypted = encrypt(message, 3)
decrypted = decrypt(encrypted, 3)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)