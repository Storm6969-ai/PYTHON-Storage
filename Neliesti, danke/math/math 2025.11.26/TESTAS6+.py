#užd6
import math
litrai = float(input("Kiek litrų kuro sunaudojama 100km?"))
atstumas = float(input("Koks kelionės atstumas kilometrais?"))
žmoniųSk = float(input("Kiek žmonių važiuoja?"))
litroKaina = float(input("Kokia kuro litro kaina (eurais)?"))

kainaŽmogui = atstumas/100*litrai*litroKaina/žmoniųSk
galas = round(kainaŽmogui % 100, 2)
print(f'Kelionės kaina vienam žmogui:{galas}€')