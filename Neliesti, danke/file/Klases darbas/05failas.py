def rasom(a, b):
    with open('05data.txt', 'w', encoding='utf-8') as f:
        f.write(str(a)+'\n')
        f.write(str(b)+'\n')

def skaitom():
    with open('05data.txt', 'r', encoding='utf-8') as f:
        x1 = int(f.readline())
        x2 = int(f.readline())
    return x1, x2

def papildom(neList):
    with open('05data.txt', 'a', encoding='utf-8') as f:
        suma = sum(neList)
        f.write(f'{neList[0]} + {neList[1]} = {suma}\n')


rasom(6, 9)
sk = skaitom()
papildom(sk)
# print(type(sk))
