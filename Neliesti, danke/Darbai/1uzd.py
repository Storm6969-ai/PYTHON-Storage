with open('tekstas.txt', 'r', encoding='utf-8') as duom:
    txt = duom.read()
    sar = txt.split(' ')
    ilgiausias = ''
    for i in sar:
        if len(i) > len(ilgiausias):
            ilgiausias = i
print(ilgiausias)