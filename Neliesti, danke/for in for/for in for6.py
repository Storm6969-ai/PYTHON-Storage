# atspausdinti visus skaicius nuo 1 iki n, bet tik iki 13

# 7, 8, 9 ,6 ,3 ,5 ,4 ,4

n = 14
for i in range(n+1):
    if i == 13:
        break         # "break" suveike tai FORo ELSEas nesuveike
    else:
        print(i, end=', ')
else:
    print(f'Ciklas suveike iki galo')