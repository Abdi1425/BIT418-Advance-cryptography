def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

message = "Cryptography"
key = 7

encrypted = xor_cipher(message, key)
decrypted = xor_cipher(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)