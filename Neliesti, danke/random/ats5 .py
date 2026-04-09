import random

kiek  = random.randint(4, 10) # kiek pazimiu
sum = 0
print("Petriuko pazimiai:")
for paz in range(kiek):
    paz = random.randint(1,10) # kokie pazimiai
    sum += paz # sudeda pazimius
    print(paz, end=', ')
vid = sum / kiek
print(f'\n o vidurkis {vid}')