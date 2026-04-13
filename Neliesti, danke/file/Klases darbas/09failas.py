moksleiviai = []
with open('09data.txt',  encoding='utf-8') as f: # pagal nutilejima open mode = 'r'
    kiekis = int(f.readline())

    for i in range(kiekis):
        eilute = f.readline()
        pazymiai = [int(x.strip()) for x in eilute.split()]
        moksleiviai.append(pazymiai)

print(moksleiviai)