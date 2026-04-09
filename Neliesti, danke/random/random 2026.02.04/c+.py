visosDienos = ['Pirmadienis', 'Antradienis']
visosKomandos = ['Vilkas','Tigras','Erelis','Lokys']
import random

for diena in visosDienos:
    print(f'{diena}:')
    visosKomandos = ['Vilkas','Tigras','Erelis','Lokys']
    for a in range(2):
        komanda = random.choice(visosKomandos)
        visosKomandos.remove(komanda)
        priesininke = random.choice(visosKomandos)
        visosKomandos.remove(priesininke)
        print(komanda, 'vs', priesininke)
    print()