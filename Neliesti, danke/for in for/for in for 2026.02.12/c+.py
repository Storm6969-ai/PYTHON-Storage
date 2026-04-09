n=999
skaiciai = range(100, n+1)

for sk in skaiciai:
    lisp = list(str(sk))
    ats = ''
    z = 0
    for i in lisp:
        z += 1
        x = ''
        x += (lisp[3-z])
        ats += x
    if str(sk) == ats:
        print(sk, end=', ')