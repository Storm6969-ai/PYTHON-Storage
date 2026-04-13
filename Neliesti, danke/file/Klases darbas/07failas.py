def kuriam(failas, info):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(info)

for i in range(1, 100):
    kuriam(f'Labas\\{i}file.bat', f'{i} faile įrašyta informacija\n')