dienos = ['Pirmadienis', 'Antradienis', 'Treciadienis', 'Ketvirtadienis', 'Penktadienis']
visosPamokos = ['Matematika','Lietuviu k.','Anglu k.','Geografija', 'Biologija']
visiKabinetai = ['(101)', '(102)', '(203)', '(305)', '(410)']
import random

for diena in dienos:
    print(f'{diena}:')
    pamokos = random.sample(visosPamokos, 4)
    kabinetas = random.choice(visiKabinetai)
    for nr, pamoka in enumerate(pamokos, start = 1):
        print(f'{nr}. {pamoka} {kabinetas}')