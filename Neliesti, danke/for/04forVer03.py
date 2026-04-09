# atspausdinti visus skaicius is intervalo [0; n]. jei pasiekiame 13 
#daugiau nespausdinti
n = int(input('n=... '))
for i in range(n+1):
    if i ==13:
        break # nutraukia visa cikla 
    print(i, end=', ')