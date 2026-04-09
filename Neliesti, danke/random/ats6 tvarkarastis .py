dienos = ['Pirmadienis', 'Antradienis', 'Treciadienis', 'Ketvirtadienis', 'Penktadienis']
pamokos = [
    'Matematika',
    'Lietuviu k.',
    'Anglu k.',
    'Geografija',
    'Fizika',
    'Fizinis',
    'Ekonomika',
    'Darbu sauga',
    'Muzika',
    'Biologija',
    'Zmogaus sauga'
    ]

import random


for diena in dienos:
    print(diena)
    at_6_Pm = random.sample(pamokos, 6) #paima random pamokas
    for nr, pamoka in enumerate (at_6_Pm, start=1):
        print(f'{nr}. {pamoka}')






