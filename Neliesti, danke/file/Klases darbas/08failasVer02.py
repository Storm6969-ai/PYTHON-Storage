def sukurti():
    with open('08data.txt', 'w') as f:
        f.write('25, 14, 48, 97, 14, 25\n')
        f.write('-14, 18, -58, 21, 45, -58, 15, 34\n')

def skaityti():
    with open('08data.txt', 'r') as f:
        x1 = f.readline()
        x2 = f.readline()
    return x1, x2

sukurti()
kazkas = skaityti()
sk = []
for eil in kazkas:
    txt = []
    txt = eil.split(', ')
    skElem = [int(i) for i in txt]
    sk.append(skElem)
print(sk)