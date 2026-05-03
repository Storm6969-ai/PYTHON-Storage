def num_0_999_to_words(n):
    """Konvertuoja skaičių 0-999 į žodžius"""
    if n == 0:
        return ""
    
    words = []
    hundreds = n // 100
    if hundreds > 0:
        match hundreds:
            case 1: words.append('vienas šimtas')
            case 2: words.append('du šimtai')
            case 3: words.append('trys šimtai')
            case 4: words.append('keturi šimtai')
            case 5: words.append('penki šimtai')
            case 6: words.append('šeši šimtai')
            case 7: words.append('septyni šimtai')
            case 8: words.append('aštuoni šimtai')
            case 9: words.append('devyni šimtai')
    
    remainder = n % 100
    
    if 10 <= remainder <= 19:
        match remainder:
            case 10: words.append('dešimt')
            case 11: words.append('vienuolika')
            case 12: words.append('dvylika')
            case 13: words.append('trylika')
            case 14: words.append('keturiolika')
            case 15: words.append('penkiolika')
            case 16: words.append('šešiolika')
            case 17: words.append('septyniolika')
            case 18: words.append('aštuoniolika')
            case 19: words.append('devyniolika')
    else:
        # Dešimtys
        tens = (remainder // 10) * 10
        if tens > 0:
            match tens:
                case 20: words.append('dvidešimt')
                case 30: words.append('trisdešimt')
                case 40: words.append('keturiasdešimt')
                case 50: words.append('penkiasdešimt')
                case 60: words.append('šešiasdešimt')
                case 70: words.append('septyniasdešimt')
                case 80: words.append('aštuoniasdešimt')
                case 90: words.append('devyniasdešimt')
        
        # Vienetai
        units = remainder % 10
        if units > 0:
            match units:
                case 1: words.append('vienas')
                case 2: words.append('du')
                case 3: words.append('trys')
                case 4: words.append('keturi')
                case 5: words.append('penki')
                case 6: words.append('šeši')
                case 7: words.append('septyni')
                case 8: words.append('aštuoni')
                case 9: words.append('devyni')
    
    return ' '.join(words)


def euro_ending(amount):
    """Nustato tinkamą euro galūnę"""
    last_two = amount % 100
    last_one = amount % 10
    
    if 10 <= last_two <= 19:
        return 'eurų'
    
    match last_one:
        case 1: return 'euras'
        case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9: return 'eurai'
        case _: return 'eurų'


def cent_ending(amount):
    """Nustato tinkamą cento galūnę"""
    last_two = amount % 100
    last_one = amount % 10
    
    if 10 <= last_two <= 19:
        return 'centų'
    
    match last_one:
        case 1: return 'centas'
        case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9: return 'centai'
        case _: return 'centų'


# Pagrindinė programa
s = input("Įveskite pinigų sumą: ")
try:
    n = float(s)
except:
    print("Neteisinga įvestis")
    exit()

if n < 0 or n > 100000:
    print("Neteisingas skaičius")
else:
    # Gauti eurus ir centus
    euros = int(n)
    cents = round((n - euros) * 100)
    
    # Konvertuoti eurus į žodžius
    if euros == 0:
        euro_words = 'nulis'
    elif euros < 1000:
        euro_words = num_0_999_to_words(euros)
    else:
        thousands = euros // 1000
        remainder = euros % 1000
        
        # Tūkstančiai
        if thousands == 1:
            thousands_word = 'vienas tūkstantis'
        elif thousands < 10:
            match thousands:
                case 2: thousands_word = 'du tūkstančiai'
                case 3: thousands_word = 'trys tūkstančiai'
                case 4: thousands_word = 'keturi tūkstančiai'
                case 5: thousands_word = 'penki tūkstančiai'
                case 6: thousands_word = 'šeši tūkstančiai'
                case 7: thousands_word = 'septyni tūkstančiai'
                case 8: thousands_word = 'aštuoni tūkstančiai'
                case 9: thousands_word = 'devyni tūkstančiai'
        else:
            # 10-99 tūkstančių
            tens_thousands = num_0_999_to_words(thousands)
            thousands_word = f"{tens_thousands} tūkstančių"
        
        euro_words = thousands_word
        if remainder > 0:
            euro_words += ' ' + num_0_999_to_words(remainder)
    
    # Suformatuoti rezultatą
    euro_form = euro_ending(euros)
    cent_form = cent_ending(cents)
    
    print(f"{euro_words} {euro_form} {cents} {cent_form}")