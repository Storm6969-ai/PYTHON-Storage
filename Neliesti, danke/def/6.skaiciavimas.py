def skaiciavimas(a, b):
    rez = a / b
    return rez

ats=skaiciavimas(5, 8)
print(ats)

x=7
y=9
ats2=skaiciavimas(x, y) #isiveda seka
print(ats2)

ats3=skaiciavimas(y, x) #skirtinga seka
print(ats3)

ats4=skaiciavimas(b=y, a=x) #grieztas nurodymas; pasikeist negali
print(ats4)
