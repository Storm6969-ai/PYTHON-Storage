# daugybos lentele iki 10

n=range(1, 11)


for i in n:
    for j in n:
        print(f'{(i*j):^3}', end='')
    print()