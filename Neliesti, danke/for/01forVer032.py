#suskaiciuoti a raides
txt = 'Mano batAi buvo du, vienas dingo - nerAndu'
skaitliukas = 0
for raide in txt:
    if  raide.lower() == 'a':
        skaitliukas += 1 # skaitliukas = skaitliukas + 1

print(f'raidziu "a" yra {skaitliukas}')
