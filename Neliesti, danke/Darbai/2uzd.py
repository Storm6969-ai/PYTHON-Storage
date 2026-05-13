with open('duomenys.txt', 'r', encoding='utf-8') as duom:
    txt = duom.read()
    txt2 = txt.replace('.', '')
    sar = txt2.split(' ')
    zodsar = []
    daugiausia = txt2[0]
    for i in sar:
        if i not in zodsar:
            zodsar.append(i)
    for y in zodsar:
        if txt2.count(y) > txt2.count(daugiausia):
            daugiausia = y
print(daugiausia)