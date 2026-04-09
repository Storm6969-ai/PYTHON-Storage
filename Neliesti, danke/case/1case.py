# UZD: Ivedama savaites diena skaiciumi (pvz 1), reikia parasyti teksto
# 1 - pirmadienis, 2 - antradienis

diena = input('Iveskite dienos skaiciu...')
# print(type(diena))

match  diena:             # 'match' iesko KAZKO kazkame
    case '1': savDiena = "pirmadienis"        # 'case' rodo imanoma varianta, ir jei taip, kazka padaro
    case '2': savDiena = "antradienis"
    case '3': savDiena = "treciadienis"
    case '4': savDiena = "ketvirtadienis"
    case '5': savDiena = "penktadienis"
    case '6': savDiena = "sestadienis"
    case '7': savDiena = "sekmadienis"
    case _: savDiena = "Blogai ivesti duomenys"   # 'case _:' rasomas jei duotas variantas netinka
print(f'{diena} diena yra {savDiena}')