import random
vaisiai = ["obuolys", "persimonas", "persikas", "apelsinas", "bananas"]

# for vaisius in vaisiai:
#     print(vaisius)

for nr, vaisius in enumerate(vaisiai, start=1): # 'start=' - parodo kuo 'enumerate' pradeda
    print(f'{nr}. {vaisius}')