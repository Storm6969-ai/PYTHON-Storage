# daugybos lentele iki 10

n=10
for i in range(n):
    print(f'Daugyba is {i}')
    for j in range(n+1):
        print(f'{i:>2} * {j:>2} = {(i*j):>3}')
    print()