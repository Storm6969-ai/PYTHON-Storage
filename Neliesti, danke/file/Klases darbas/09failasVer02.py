# su validacija

with open('09data.txt',  encoding='utf-8') as f: # pagal nutilejima open mode = 'r'
    eilutes = f.readlines()

kiekis = int(eilutes[0].strip())
duomenys = eilutes[1:]

if len(duomenys) != kiekis:
    raise ValueError('Nesutampa kiekis')

mokiniai = [
    [int(x) for x in eilute.split()]
    for eilute in duomenys 
]

print(mokiniai)