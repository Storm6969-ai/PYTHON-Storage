# turim trys lazdas , ar is lazdu galima sudaryti trikampi
a = float(input('koks a?...'))
b = float(input('koks b?...'))
c = float(input('koks c?...'))
if (a < b + c) and (c < a + b) and (b < a + c) and (a > 0 and b > 0 and c > 0):
   print(f'trikampis, kurio krastines {a}, {b}, {c} galimas')
else:
   print(f'trikampis, kurio krastines {a}, {b}, {c} negalimas')