l = input('Kokia lytis? (M/V)   ')
a = int(input('Koks amzius?    '))

match l:
    case 'M':
        match a:
            case a if 0<=a<7:
                x = 'Mergaite'
            case a if 7<=a<=18:
                x = 'Mergina'
            case a if 18<a:
                x = 'Moteris'

    case 'V':
        match a:
            case a if 0<=a<7:
                x = 'Berniukas'
            case a if 7<=a<=18:
                x = 'Bernas'
            case a if 18<a:
                x = 'Vyras'

    case _:
        x = 'Klaida'
print(x)