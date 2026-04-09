a=5
5
sk=int(input('Ivesk skaiciu '))
# 'sk =int(sk)' - pakeičia 'sk' iš str į int
print(type(sk)) #input grazina string ne int
print(sk)
a, b, c =input('Ivesk skaicius atskirtus kableliais ').split(',') ## '.split(x)' - rodo kuo atskirti kintamuosius, 'x' rodo koks rašomas skirtukas
b=int(b)
print(b)
print(type(b))
