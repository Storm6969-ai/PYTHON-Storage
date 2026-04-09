sk = float(input('x=...'))
# arLaimingas = (sk>=5 and sk<=10) or (sk>=20 and sk<=25)

arLaimingas = (5<=sk<=10) or (20<=sk<=25)

if arLaimingas:
    print(f'Skaicius {sk} yra laimingas')
else:
    print(f'Skaicius {sk} yra NE-laimingas')