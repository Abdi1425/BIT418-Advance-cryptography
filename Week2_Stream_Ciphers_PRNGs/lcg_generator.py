class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

generator = LCG(1)

for _ in range(10):
    print(generator.next())