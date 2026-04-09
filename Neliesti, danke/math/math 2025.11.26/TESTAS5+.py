#užd5
import math
k11 = int(input("Kiek kilogramų Petriukas pririnko per 1 dieną?"))
k12 = int(input("Kiek gramų Petriukas pririnko per 1 dieną?"))
k21 = int(input("Kiek kilogramų Petriukas pririnko per 2 dieną?"))
k22 = int(input("Kiek gramų Petriukas pririnko per 2 dieną?"))

šilauogėsGramais = k12+k22+(k11+k21)*1000


kilogramaiŠilauogių = šilauogėsGramais // 1000
gramaiŠilauogių = šilauogėsGramais % 1000

print(f'Iš viso Petriukas pririnko {kilogramaiŠilauogių} kg ir {gramaiŠilauogių} g Šilauogių')