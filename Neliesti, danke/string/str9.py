# from sys import getsizeof

# sarasas = [i for i in range(10000)]
# gen = (i for i in range(10000))
# x = getsizeof(sarasas)
# y = getsizeof(gen)
# print(f'sar = {x}, gen = {y}')  ## gen yra 400 kartu uzima maziau duomenu

import timeit
sar2 = [i for i in range(10000) if i % 2 == 0]
gen2 = (i for i in range(10000) if i % 2 == 0)
print(timeit.timeit('''[i for i in range(100) if i % 2 == 0]''', number=100000))
print('vs')
print(timeit.timeit('''(i for i in range(100) if i % 2 == 0)''', number=100000))