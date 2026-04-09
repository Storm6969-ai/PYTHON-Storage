# nustatyti koks ivestas pazimys
# 1, 2, 3 --- blogai
# 4, 5, 6 --- patenkinama
# 7. 8. 9  --- gerai
# 10 --- puiku
# visi kiti --- netenkinami duomenys

paz = int(input('Koks pazimys...'))
match paz:
    # case 1: rez = 'Blogai'
    # case 2: rez = 'Blogai'
    # case 3: rez = 'Blogai'
    case 1 | 2 | 3 : rez = 'Blogai'
    case 4 | 5 | 6 : rez = 'Patenkinamai'
    case 7 | 8 | 9 : rez = 'Gerai'
    case 10 : rez = 'Puiku'
    case _: rez =  'Blogi duomenys'
print(f'{paz} → {rez}')