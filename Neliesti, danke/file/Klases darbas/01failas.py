with open('01byla.txt', 'w', encoding='utf-8') as f:
    f.write('Pirmas kartas su byla...')
    a = 5
    f.write(f'a={a}')
    sar = [1, 2, 3, 4]
    f.write(f'Petriuko pazymiai: {sar}\n')
    print('Petriuko pazymiai',*sar, file=f)
    print('kita eilutė', file=f)
    print(*sar, sep=', ', file=f)
    print(f.closed)
# f.write('Labas')

# print(f.closed)
