pazimiuKiekis = int(input('Kiek pažymių?...'))
visiPaz = []
suma = 0
neigiamuKiekis = 0
teigiamuKiekis = 0
didesniuUzSeptynis = 0

for x in range(pazimiuKiekis):
    paz = 0
    paz = int(input(f'Įveskite {x+1}-ąjį pažymį: '))
    suma = suma + paz
    visiPaz.append(paz)

    if paz >= 4:
        teigiamuKiekis = teigiamuKiekis + 1
    else:
        neigiamuKiekis = neigiamuKiekis + 1

    if paz > 7:
        didesniuUzSeptynis = didesniuUzSeptynis + 1

print()
print('Vidurkis: ', suma / len(visiPaz))
print('Teigiamų pažymių kiekis: ', teigiamuKiekis)
print('Neigiamų pažymių kiekis: ', neigiamuKiekis)
print('Didžiausias pažymys: ', max(visiPaz))
print('Pažimių didesnių už 7: ', didesniuUzSeptynis)