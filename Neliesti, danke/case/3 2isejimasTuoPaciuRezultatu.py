# Ivedamas menesis kaip skaicius, nustatytis menu laika ir trumpus tendencijas patarimus

laikas = int(input('Koks menuo...'))

match laikas:
    case 12|1|2:
        rengimas = 'siltai'
        temperatura = 'salta'
    case 3|4|5:
        rengimas = 'apyvesiai'
        temperatura = 'vidutine'
    case 6|7|8:
        rengimas = 'vesiai'
        temperatura = 'silta'
    case 9|10|11:
        rengimas = 'apyvesiai'
        temperatura = 'vidutine'
print(f'rengtis {rengimas}, temperatura yra{temperatura}')