skaiciai = []
suma = 0
x = input('Įvesk 5 skaičius...')
for y in x:
    suma = suma + int(y)
    skaiciai.append(int(y))

print('Skaičiai:', skaiciai)
print('Suma:', suma)
print('Vidurkis:', suma / len(skaiciai))
print('did + min:', max(skaiciai) + min(skaiciai))