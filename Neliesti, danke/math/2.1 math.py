#duoda stataus trikampio a ir c. Rasti plota
import math
a1=float(input('a= '))
c1=float(input('c= '))
#b=math.sqrt(math.pow(c,2)-math.pow(a,2))
#b=math.sqrt(c*c-a*a)
b1=math.sqrt(c1**2-a1**2)
plotas=a1*b1/2
print(plotas)

# arba


a = float(input("Iveskite statines a ilgi..."))
c = float(input("Iveskite statines c ilgi..."))

b = math.sqrt(c**2 - a**2)
S = a*b/2

print(f'Trikampio plotas = {S}')