# Diffie-Hellman Key Exchange

# Public values
p = int(input("Enter prime number (p): "))
g = int(input("Enter generator (g): "))

# Private keys
alice_private = int(input("Enter Alice's private key: "))
bob_private = int(input("Enter Bob's private key: "))

# Public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

# Shared secrets
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

print("\nAlice Public Key:", alice_public)
print("Bob Public Key:", bob_public)
print("Alice Shared Secret:", alice_secret)
print("Bob Shared Secret:", bob_secret)

if alice_secret == bob_secret:
    print("\nKey Exchange Successful!")
else:
    print("\nKey Exchange Failed!")