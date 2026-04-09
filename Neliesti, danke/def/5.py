# 5 + 8 = 13
# skt1=int(input('ski1=...'))
# skt2=int(input('ski1=...'))
# rez = skt1 +skt2
# print(f'{skt1}+{skt2}={rez}')

def ivedimas(txt):
    sk = int(input(f'{txt} = .... '))
    return sk

def skaiciavimas(a, b):
    ats = a + b
    return ats

def spausdinimas():
    sk1=ivedimas('ski1')
    sk2=ivedimas('ski1')
    rez = skaiciavimas(sk1, sk2)
    print(f'{sk1}+{sk2}={rez}')




spausdinimas()