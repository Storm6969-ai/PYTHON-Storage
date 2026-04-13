# su validacija

with open('09data.txt',  encoding='utf-8') as f: # pagal nutilejima open mode = 'r'
    kiekis = int(f.readline())
    mokiniai = [
        [int(x) for x in f.readline().split()]
        for _ in range(kiekis) 
        ]

print(mokiniai)