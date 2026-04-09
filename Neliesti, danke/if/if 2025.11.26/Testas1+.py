T1 = int(input('Kiek davė pirmas teisėjas?...'))
T2 = int(input('Kiek davė antras teisėjas?...'))
T3 = int(input('Kiek davė trečias teisėjas?...'))
T4 = int(input('Kiek davė ketvirtas teisėjas?...'))


if T1>=T2 and T1>=T3 and T1>=T4:
    did = T1
elif T2>=T3 and T2>=T4:
    did = T2
elif T3>=T4:
    did = T3
else:
    did = T4

if T1<=T2 and T1<=T3 and T1<=T4:
    maz = T1
elif T2<=T3 and T2<=T4:
    maz = T2
elif T3<=T4:
    maz = T3
else:
    maz = T4

teisejuBalas = (T1+T2+T3+T4-(did+maz))/2
print(teisejuBalas)