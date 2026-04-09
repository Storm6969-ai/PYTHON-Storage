# n=10
# skaiciai = range(1, n+1)
# for sk in skaiciai:
#     puseSk = sk // 2
#     print(f'{sk}-→', end=' ')
#     x = 0
#     for i in range(1, puseSk+1):
#         if sk % i == 0:
#             print(i, end=' ')
#             x += i
#             print(f"({x})", end=', ')
#     if sk == x:
#         print('CORRECT', end=' ')
#     print()


# n=1000
# skaiciai = range(1, n+1)
# for sk in skaiciai:
#     nr1 = nr2 = nr3 = nr4 = 0
#     if sk<10:
#         x = 1
#         nr1 = sk ** x
#     elif sk < 100:
#         x = 2
#         nr2 = (sk%10)**x;  nr1 = (sk//10)**x
#     elif sk < 1000:
#         x = 3
#         nr3 = (sk%10)**x; nr2 = (sk//10%10)**x; nr1 = (sk//100%10)**x
#     elif sk == 1000:
#         x = 4
#         nr4 = (sk%10)**x; nr3 = (sk//10%10)**x; nr2 = (sk//100%10)**x; nr1 = (sk//1000%10)**x
#     ats = nr1 + nr2 + nr3 + nr4
#     if ats == sk:
#         print(sk, end=', ')

#     # print(f'{sk:^4} ←→ {x} ←→{nr1:^4}+{nr2:^4}+{nr3:^4}+{nr4:^4}= {ats}')





# n=999
# skaiciai = range(100, n+1)

# for sk in skaiciai:
#     lisp = list(str(sk))
#     ats = ''
#     z = 0
#     for i in lisp:
#         z += 1
#         x = ''
#         x += (lisp[3-z])    ## can be used to count any number if you replace '3' with 'len(lisp)'
#         ats += x
#     if str(sk) == ats:
#         print(sk, end=', ')