txt = "2025 metais 3C grupė turi 28 mokinius"
kiekis = 0

for skaičius in txt:
    if skaičius in '012356789':
        kiekis += 1
print(f'{kiekis}')