h = int(input('Kokia valanda? (0-23)    '))
a = int(input('Koks amzius?    '))

match h:
    case h if 8<=h<=16:
        match a:
            case a if 0<=a<7:
                x='0€'
            case a if 7<=a<=18:
                x='3€'
            case a if a>18:
                x='5€'
            case _:
                x='KLAIDINGA'
        print(f'Pagrindine kaina yra {x}')
    case h if 17<=h<=22:
        match a:
            case a if 0<=a<7:
                x='0€'
            case a if 7<=a:
                x='4€'
            case _:
                x='KLAIDINGA'
        print(f'Vakarine kaina yra {x}')
    case h if 0<=h<=7 or h==23:
        print('uzdaryta')
    case _:
        print('klaidinga informacija')