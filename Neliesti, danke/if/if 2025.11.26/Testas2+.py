m = int(input('Matematikos pazimys =...'))
lk = int(input('Lietuviu kalbos pazimys =...'))
it = int(input('Informaciniu technologiju pazimys =...'))

vidurkis = (m+lk+it)/3

if m>=4 and lk>=4 and it>=4:
    if vidurkis>=9:
        print('Puikiai!')
    elif vidurkis>=7:
        print('Gerai')
    else:
        print('Patenkinama')
else:
    print('Neislaikyta')