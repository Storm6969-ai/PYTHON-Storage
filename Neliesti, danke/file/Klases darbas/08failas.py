def sukurti():
    with open('08data.txt', 'w') as f:
        f.write('25, 14, 48, 97, 14, 25\n')
        f.write('-14, 18, -58, 21, 45, -58, 15, 34\n')

def skaityti():
    with open('08data.txt', 'r') as f:
        viskas = f.read()
    return viskas

sukurti()
kazkas = skaityti()
print(kazkas)
txt = kazkas.split('\n')
print(txt)