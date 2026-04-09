txt = "Labas Rytas, mokiniai!"
kiekis = 0

for raide in txt:
    if raide.lower() in 'bcčdfghklmnprsštvz':
        kiekis += 1
print(f'{kiekis}')