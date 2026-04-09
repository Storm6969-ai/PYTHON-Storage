# parasyti programa kur atspausdina zodi "aciu" n kartu

## Kaip padaryti su FOR
# n = 15
# for i in range(n):
#     print("aciu", end=', ')



n = 15     # kiek kartu
ck = 0     # privalo buti nuo 0
while ck < n:          # kol ck < n, tol ciklins
    print("Aciu", end=', ')
    ck = ck + 3            # po kiekvieno ciklo prideda, gale ck > n
else:
    print('Ciklas suveike iki galo')