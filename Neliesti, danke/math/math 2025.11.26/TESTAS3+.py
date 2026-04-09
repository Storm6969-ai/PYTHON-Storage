#užd3
import math
m1 = int(input("Kiek yra monetų po 1 ct?"))
m2 = int(input("Kiek yra monetų po 2 ct?"))
m3 = int(input("Kiek yra monetų po 5 ct?"))
m4 = int(input("Kiek yra monetų po 10 ct?"))
m5 = int(input("Kiek yra monetų po 50 ct?"))

suma = (1*m1 + 2*m2 + 5*m3 + 10*m4 + 50*m5) 
sumaEurais = suma / 100
print(f"Taupyklėje yra {sumaEurais:.2f}€")