#Ivedami 2 skaiciai ir operacija (pvz +, -, /, *)
# apskaiciuoti ir atspausdinti rezultata

op = input('Kokia operacija...')
sk1 = int(input('Koks pirmas skaicius...'))
sk2 = int(input('Koks antras skaicius...'))


match op:
    case '+':
        oper = sk1+sk2
        print(f'{sk1} {op} {sk2} = {oper}')
    case '-':
        oper = sk1-sk2
        print(f'{sk1} {op} {sk2} = {oper}')
    case '*':
        oper = sk1*sk2
        print(f'{sk1} {op} {sk2} = {oper}')
    case '/':
        match sk2:                                    #2-as 'match' viduje 'case'
            case 0: print('Neimanomas')
            case _:
                oper = sk1/sk2
                print(f'{sk1} {op} {sk2} = {oper}')
    case _: print('Neimanoma')