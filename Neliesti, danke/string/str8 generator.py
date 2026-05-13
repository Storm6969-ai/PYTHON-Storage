skLyg = [i for i in range(21) if i % 2 == 0] ## užima daug vietos
# print(skLyg)
suma = sum(skLyg)
print(suma)


skNelyg = (i for i in range(21) if i % 2 != 0) ## užima MAŽAI vietos
# print(skNelyg)
# suma2 = sum(skNelyg)
# print(suma)
print(next(skNelyg))
print(next(skNelyg))
print()
for i in skNelyg:
    print(i) ## pradeda spaudinti nuo '5', nes  '1' ir '3' jau issapusdinti

for i in skNelyg:
    print(i)