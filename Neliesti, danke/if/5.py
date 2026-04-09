# nustatyt iar skaicius didesnis uz 0, kei traip - apskaiciuoti jo kuba
# jei mazesnis - jo kvadrata, jei nulis tai parasom "bazaras"

sk = int(input('sk=...'))
kv = sk ** 2
if sk > 0:
    print(f'skaiciu {sk} didesnis uz nuli {kv}') 
    ats = sk**3
    print(f'skaiciu {sk } pakele kubu gausim {ats}')
elif sk < 0:
    print(f'skaicius {sk} mazesnis uz nuli') 
    ats = sk**2
    print(f'skaiciu {sk } pakele kvadratu gausim {ats}')
else:
    print('bazaras')
    ats = 0
    print(f'jus ivedete skaiciu {sk } atsakymas {ats}')

print('---------------------')