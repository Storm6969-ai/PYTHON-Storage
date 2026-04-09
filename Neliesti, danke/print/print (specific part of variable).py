#turime penkiazenkli sk rasti jo skaitmenu suma
#list, for, while naudoti negalim
sk=int(input('Penkiazenklis skaicius = '))
x1=sk//10000 %10
x2=sk//1000 %10
x3=sk//100 %10
x4=sk//10 %10
x5=sk%10
sum=x1+x2+x3+x4+x5
print(x1, x2, x3, x4, x5)
print(f'Skaiciaus {sk} skaitemnu suma lyg {sum}')