# Simple SPN Cipher

sbox = {
    '0': 'E',
    '1': '4',
    '2': 'D',
    '3': '1',
    '4': '2',
    '5': 'F',
    '6': 'B',
    '7': '8',
    '8': '3',
    '9': 'A'
}

plaintext = input("Enter a number: ")

# Substitution
substituted = ""
for char in plaintext:
    substituted += sbox.get(char, char)

print("After Substitution:", substituted)

# Permutation
ciphertext = substituted[::-1]

print("Ciphertext:", ciphertext)