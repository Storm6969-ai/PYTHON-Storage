import random
ats = random.random() # nuo 0 iki 1 sukuria random
print(round(ats*100,0))

atsInt = random.randint(-100, 100) # random skaicius nuo -100 iki 100
print(atsInt)

atsRange = random.randrange(0, 100, 5) # random sk nuo 0 iki 100 kas penkta
print(atsRange)

# !iki 100 reiskia max bus "99"