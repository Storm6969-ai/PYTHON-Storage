a = int(input('a ilgis....'))
b = int(input('b ilgis....'))
c = int(input('c ilgis....'))
d = int(input('d ilgis....'))

if a == b and c == d:
    print('Kurmiui žemės sklypo ribas pažymėti pavyks')
elif a == c and b == d:
    print('Kurmiui žemės sklypo ribas pažymėti pavyks')
elif a == d and b == c:
    print('Kurmiui žemės sklypo ribas pažymėti pavyks')
else:
    print('Kurmiui žemės sklypo ribų pažymėti nepavyks')