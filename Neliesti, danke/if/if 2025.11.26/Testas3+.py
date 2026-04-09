leistinasGreitis = int(input('Iveskite leistina greiti (km/h)...'))
vairuotojoGreitis = int(input('Iveskite savo greiti (km/h)...'))

x = vairuotojoGreitis - leistinasGreitis

if x>0:
    print(f'Virsyta {x}km/h')
    if x<=10:
        print('Ispejimas')
    elif 11<=x<=30:
        print('Bauda: 30€')
    elif 31<=x<=50:
        print('Bauda: 100€')
    else:
        print('Bauda: 300€ ir pazimejimo atemimas')
else:
    print('Leistinas greitis')