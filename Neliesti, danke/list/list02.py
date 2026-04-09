skar = [5, 8, 7, 4, 5, 10, 9]

kiekis = 0; suma = 0; didPaz = skar[0]
for paz in skar:
    print(paz)
    suma += paz
    kiekis += 1
    if paz > didPaz:
        didPaz = paz


kiekis = len(skar); suma = sum(skar); didPaz = max(skar)


vidurkis = suma / kiekis
print(f'Vidurkis: {vidurkis}')
print(F'Didziausias paz: {didPaz}')