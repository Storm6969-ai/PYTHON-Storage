p1 = int(input('p1= ...'))
if p1<1 or p1>10:
    print('pakartokite ivedima')
    p1 = int(input('p1= ...'))
p2 = int(input('p2= ...'))
p3 = int(input('p3= ...'))
suma = p1 + p2 + p3
vidurkis = suma / 3
print(f'Pretriuko vidurkis {vidurkis:.3f}') ## ':.3f' - rodo kiek skaičių rodyti po kablelio