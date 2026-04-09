visosPamokos = ['Matematika','Lietuviu k.','Anglu k.',]
visiMokiniai = ['Jomas', 'Ieva', 'Mantas']
import random

for mokinys in visiMokiniai:
    print(f'{mokinys}:')
    for pamoka in visosPamokos:
        paz = random.randint(0,10) # kokie pazimiai
        print(f'{pamoka} - {paz}')
    print()