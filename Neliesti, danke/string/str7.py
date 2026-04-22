# #raides, skaiciai, kiek ko?
# txt = input('Iveska bet ka')

# sarTXT = [simbolis for simbolis in txt if simbolis.isalpha()]
# print(sarTXT)
# txt2 =''.join(sarTXT)
# print(txt2)


# sarNUM = [simbolis for simbolis in txt if simbolis.isdigit()]
# print(sarTXT)
# txt3 =''.join(sarNUM)
# print(txt3)


# sarNeNUM_NeTXT = [simbolis for simbolis in txt if not(simbolis.isalnum())]
# print(sarNeNUM_NeTXT)
# txt4 =''.join(sarNeNUM_NeTXT)
# print(txt4)

# txt = input('Iveska bet ka')
# # kiekRaidziu = sum(1 for simbolis in txt if simbolis.isalpha())
# kiekRaidziu = sum(1 for _ in txt if _.isalpha())
# print(kiekRaidziu)

t = 'L4b4s ryt4s'
kazkas = (simbolis for simbolis in t if simbolis.isalpha())
print(kazkas)

for i in kazkas:
    print(i)


print(next(kazkas))
print(next(kazkas))
for i in kazkas:
    print(i)