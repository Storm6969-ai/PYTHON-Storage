# ivedami 3 skaiciai, rasti didziausi
a = int(input('a=...'))
b = int(input('b=...'))
c = int(input('c=...'))

if a >= b and a >= c:
    did = a
elif b>= c:
    did = b
else:
    did = c
print(f'Didziausias skaicius yra {did}')