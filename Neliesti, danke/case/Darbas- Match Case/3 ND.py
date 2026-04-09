svoris = float(input('Koks jusu svoris? (kg)    '))
ugis = float(input('Koks jusu ugis? (m)    '))

KMI = svoris / (ugis**2)

match KMI:
    case KMI if KMI<18.5:
        x='Nepakankamas svoris'
    case KMI if 18.5<=KMI<=24.9:
        x='Normalus svoris'
    case KMI if 25<=KMI<=29.9:
        x='Antsvoris'
    case KMI if 30<=KMI:
        x='Nutukimas'
    case _:
        x='Netinkami duomenys'
print(round(KMI, 2))
print(x)