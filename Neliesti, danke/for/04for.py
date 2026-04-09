# atspausdinti visus skaicius is intervalo [0; n]. jei pakliuna skaicius 13
#jo nespausdinti
n = int(input('n=... '))
for i in range(n+1):
    if i !=13:
        print(i, end=', ')