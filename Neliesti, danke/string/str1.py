print('sdfdf "daug" teksto \' ir \' ivairiu kabuciu \new')
print('C:\\newFolder\\newData.txt')

txt = 'Labas rytas'
print(txt[1])
print(txt[-1]);  print(txt[len(txt)-1]) # abu tas pats

print(len(txt))

# txt[0] = 'A'   'nepavykas'

print(txt[:5]) # pirmi 5
print(txt[5:]) # nuo 5 iki galo
print(txt[::2]) # visi bet kas antras

print(txt[2:13:2]) # nuo 2 iki 10 kas 3

txt2 = txt
print(txt2)
print(id(txt), id(txt2))

txt3 = txt + ' ' # jei '' tuscia, tai tampa kopija
print(txt3)
print(id(txt), id(txt3))
txt3 = txt3.strip()
print(id(txt), id(txt3))