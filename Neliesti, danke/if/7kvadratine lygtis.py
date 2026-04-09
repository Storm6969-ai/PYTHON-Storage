# ax*x + bx + c = 0  rasti sprendinius

import math
a = float(input('a=...'))
b = float(input('b=...'))
c = float(input('c=...'))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f'Atsakymas: x1 = {x1:.3f}, x2 = {x2:.3f}') # '.3f' rodo kiek poziciju po kablelio rodyti

elif D == 0:
    x = -b / (2*a)
    print(f'Atsakymas: x = {x:.3f}')
else:
    print('lygtis neturi sprendiniu')
