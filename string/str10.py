# p1 = 3.1415698
# kaina = 4.5678
# kaina1 = 4.5
# procentai = 0.85321

# print(f'Skaicius PI su dviem skaitemnimis po kablelio {p1:.2f}')
# print(f'Kaina {kaina:.2f}')
# print(f'Kaina {kaina1:.2f}')

# x = 42
# print(f'|{x:20}|')
# print(f'|{x:^20}|')
# print(f'|{x:<20}|')
# print(f'|{x:>20}|')

# val = 5; min = 2
# print(f'{val:02}:{min:02}')

# for id in range(10):
#     print(f'id → {id:04}', end=" ")

sk = 255
print(f'Devtainis {sk:b}') ## isveda binarini koda
print(f'Astuntainis {sk:o}') ## isveda astuntaini koda
print(f'Sesioliktainis {sk:x}') ## isveda sesioliktaini koda

r = 243; g = 8; b = 11
hex_spalva =  f'#{r:02X} {g:02X} {b:02X}'
print(f'RGB({r}, {g}, {b}) → {hex_spalva}')