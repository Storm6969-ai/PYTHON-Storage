x = [8, 5, 9, 7, 6, 5, 3, 4, 2]
y = x # 'y' padaro nuoroda į 'x', o ne sukuria kopija

z = x.copy()

print('y:', y)
y.append(1000) # priskiri prie saraso
print("(pakeistas y) x:", x) 

print('pirminio x kopija: ', z)


a = 5
b = a
b = 100 # vienas variable tiesiog perrasomas
print(a)