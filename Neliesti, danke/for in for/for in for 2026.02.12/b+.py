n=10000
skaiciai = range(1, n+1)

for sk in skaiciai:
    puseSk = sk // 2
    x = 0
    for i in range(1, puseSk+1):
        if sk % i == 0:
            x += i
    if sk == x:
        print(f'{sk} is correct', end='     ')