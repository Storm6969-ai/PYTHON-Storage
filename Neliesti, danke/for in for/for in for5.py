# atspausdinti visus pirminius sk is intervalo [1, n]

# 1 Nustatyti ar pirminis
    # 1.1 atspausdinti visus skaicius iki n


# for i in range(n+1):
#     print(i, end = ", ")

    # 1.2 Reikia visus daliklius skaiciaus n
#   for i in range(1, n+1):
#       if n % i == 0:
#           print(i, end = ", ")

    # 1.3 suskaiciuoti visus skaiciaus n dalklius
# kiekis =  0 
# for i in range(1, n+1):
#   if n % i == 0:
#     print(i, end = ", ")
#     kiekis = kiekis + 1
# print(f'Dalikliu skaicius {kiekis}')

    # 1.4 Ar skacius pirminis
# n = 100000000
# kiekis =  0 
# for i in range(1, n+1):
#   if n % i == 0:
#     kiekis = kiekis + 1
# if kiekis == 2:
#   print(f'Skacius {n} pirminis')
# else:
#   print(f'Skacius {n} sudetinis')

#     # 1.5 Ar skaicius pirminis (PAGREITINTI)
# n = 100000000
# kiekis =  0 
# for i in range(2, n//2):
#   if n % i == 0:
#     kiekis = kiekis + 1
# if kiekis == 2:
#   print(f'Skacius {n} pirminis')
# else:
#   print(f'Skacius {n} sudetinis')

#     # 1.6 Ar skaicius pirminis (DAAR PAGREITINTI)
# pirminis = True

# n = 10000001
# kiekis =  0 
# for i in range(2, n//2):
#   if n % i == 0:
#     pirminis = False
#     break
# if pirminis:
#   print(f'Skacius {n} pirminis')
# else:
#   print(f'Skacius {n} sudetinis')

#     # 2 atspausdinti visus pirminius sk is intervalo [1, n]
# n = 10001
# for sk in range(1, n+1):
#     pirminis = True
#     puseSk = sk // 2
#     for i in range(2, puseSk+1):
#         if sk % i == 0:
#             pirminis = False
#             break
#     if pirminis:
#         print(sk, end = ', ')

    # 2 atspausdinti visus pirminius sk is intervalo [1, n]
n = 1000
for sk in range(1, n+1):
    puseSk = sk // 2
    for i in range(2, puseSk+1):
        if sk % i == 0:          #sveikai pasidalins tik sudetinai, kurie trigerins BREAK ir tada nebus print
            break
    else:
        print(sk, end = ', ')