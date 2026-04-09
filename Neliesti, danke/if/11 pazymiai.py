# idedamas 1 pazimys
# -BEGALYBE iki 0  = negalimas pazimys
# 1 iki 3 = nepatenkinamas
# 4 iki 6 = patenkinmas
# 7 iki 9 = geras
# 10 = puikus
# 11 iki +BEGALYBE

paz = int(input('Koks pazimys?...'))

if 1<=paz<=3:
    print('Pazimys yra NEPATENKINAMAS')
elif 4<=paz<=6:
    print('Pazimys yra PATENKINAMAS')
elif 7<=paz<=9:
    print('Pazimys yra GERAS')
elif paz == 10:
    print('Pazimys yra PUIKUS')
else:
    print('Negalimas Pazimys')