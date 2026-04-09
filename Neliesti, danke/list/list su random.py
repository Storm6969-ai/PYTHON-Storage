import random


kiek = random.randint(20, 25)
print(kiek)
paz = []
for p in range(kiek):
    sk = random.randint(4, 10)
    paz.append(sk)
print(paz)

paz2 = [random.randint(3, 10) for _ in range(random.randint(10, 25))]
print(paz2)