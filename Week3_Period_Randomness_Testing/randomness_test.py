import random

bits = [random.randint(0,1) for _ in range(100)]

ones = bits.count(1)
zeros = bits.count(0)

print("Ones:", ones)
print("Zeros:", zeros)

runs = 1

for i in range(1, len(bits)):
    if bits[i] != bits[i-1]:
        runs += 1

print("Runs:", runs)

mean = sum(bits)/len(bits)

print("Mean:", mean)