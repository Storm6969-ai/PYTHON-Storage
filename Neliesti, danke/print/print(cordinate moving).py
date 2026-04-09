a=14
print(type(a))
print('a= ', a)

x1=x2=x3=5  ## visiem kintamiejam duodama ta pati reišmė
print('x1 =', x1, 'x2 =', x2, 'x3 =', x3)

sk1,sk2,sk3=5,8,7
print('sk1 =', sk1, 'sk2 =', sk2, 'sk3 =', sk3)
print(f'sk = {sk1} sk2 = {sk2} sk3 = {sk3}') #formatuotas eilutes isvedimo budas
print('mano skaiciai', sk1, sk2, sk3)
print('mano skaiciai', sk1, sk2, sk3, sep= ' | ', end = ' |\n') # 'sep' - skyriklis po kiekvieno kablelio
print(sk1+sk2)

y=8.547854
print(type(y))
print(f'|{y}|')
print(f'|{y:20}|') #duoda 20 vietu skaiciui
print(f'|{y:^20}|') #^centruoja per vidury
print(f'|{y:<20}|') #centruoja kaireje
print(f'|{y:>20}|') #centruoja desineje
