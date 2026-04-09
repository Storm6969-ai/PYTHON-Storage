#pinigai i eu ir cnt
Sumacnt=int(input('kiek radote centu? '))
eu=Sumacnt//100
centai=Sumacnt%100
print(f'{Sumacnt}cnt = {eu}eur {centai}cnt')


print('---------------------------------')
# 125ct = 1 eur. 25ct
#1458ct = 14eur58ct
#xct = x//100 eur x-x/100 ct
pinigusuma = int(input('Iveskite suma centais...'))
eura = pinigusuma //100 #rodo pirmus skaičius
centai = pinigusuma % 100 #rodo paskutinius pagal nulių skaičių
print(f'{pinigusuma}ct={eura}eur.{centai}ct')