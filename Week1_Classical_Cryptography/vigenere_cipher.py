def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char

    return result

print(encrypt("HELLO", "KEY"))