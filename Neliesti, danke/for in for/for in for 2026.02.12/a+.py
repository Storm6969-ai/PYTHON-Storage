n=1000
skaiciai = range(1, n+1)

for sk in skaiciai:
    ats = 0
    for y in str(sk):
        if sk<10: x=1
        elif sk<100: x=2
        elif sk<1000: x=3
        elif sk==1000: x=4
        z = 0
        z = int(y)**x
        ats += z
    if ats == sk:
        print(sk, end=', ')

    # print(f'{sk:^4} ←→ {x} ←→{nr1:^4}+{nr2:^4}+{nr3:^4}+{nr4:^4}= {ats}')