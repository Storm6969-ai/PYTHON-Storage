# suskaiciuoti ir atspausdinti 5 pirmas abeceles raides, esancias
# sakinyje
penkiosRaides = 'aąbcč'  
txt = 'Mano batai buvo du, vienas dingo - nerandu'
kiek = 0
for raide in txt:
    if raide.lower() in penkiosRaides:
        print(raide, end=', ')
        kiek += 1
print(f'Ju yra {kiek}')