a=None
print(a, "→", type(a), "\n") ## <class 'int'>

b=5
print(b, "→", type(b), "\n")  ## <class 'int'>

c=5,5656 ## 'x,y' ėma 'x' ir 'y' kaip skirtingus dalykus
print(c, "→", type(c), "\n") ## <class 'tuple'>

d=True
print(d, "→", type(d), "\n") ## <class 'bool'>

e=5.25454
print(e, "→", type(e), "\n") ## <class 'float'>

f='tekstas'
print (f, "→", type(f), "\n") ## <class 'str'>

g=['Jonas', 26, 4.75, True, 'Ieva', 24, 1457.78, True]
print (g, "→", type(g), "\n") ## <class 'list'>

h=[14,8,7,5,9,1,4,14,9,7]
print(h)
print(h[0], "\n") ## 'h[0]' - paėma pirmą elemtąą iš 'h' sąrašo

j=5-1j
print (j, "→", type(j), "\n") ## <class 'complex'>