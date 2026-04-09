# if salyga arba loginis reiskinys:
#     veiksmai kai teisinga salyga
# else:
#     veiksmai kai salyga neteisinga



#apskaiciuoti skaiciaus kvadrata jei sk == 13 isvesti pranesima "laimingas skaucius", bet ir apskaiciuoti kvadrata
    

sk = int(input('sk=...'))
kv = sk ** 2
if sk == 13:
    print('Laimingas Skaicius')
    print('Bet kvadrata vistiek skaiciuosim')
print(f'skaiciu {sk} pakelus kvadratu gausim {kv}') #vyksta nesvarbu rezultato