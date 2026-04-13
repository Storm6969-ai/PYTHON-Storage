with open('04data.txt', 'r', encoding='utf-8') as f:
    sar1 = [int(x) for x in f.readline().split()]
    # sar2 = [int(x) for x in f.readline().split()]
    sar2 = []
    eilute = f.readline()
    for x in eilute.split():
        sar2.append(int(x))

print(sar2)