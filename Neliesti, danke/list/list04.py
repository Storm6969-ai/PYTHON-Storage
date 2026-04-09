txt = '25 40 35 14 26'
# skar = list(txt)
skar = list(txt.split(' ')) # .split() - nurodo koks skirimas
print(skar)

# sar = []
# skaiciaiTxt = list(txt.split(' '))
# for sk in skaiciaiTxt:
#     sar.append(int(sk))
# print(sar)


sar2 = [int(sk) for sk in list(txt.split())]
print(sar2)

far2 = [2, 4, 5, 8, 9]
# n = []
# for sk in far2:
#     n.append(sk ** 2)
# print(n)

n2 = [sk**2 for sk in far2]
print(n2)