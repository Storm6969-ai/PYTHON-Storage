#užd4
import math
s11 = int(input("Kiek centimetrų sraigė nučliaužė 1 minutę?"))
s12 = int(input("Kiek miliimetrų sraigė nučliaužė 1 minutę?"))
s21 = int(input("Kiek centimetrų sraigė nučliaužė 2 minutę?"))
s22 = int(input("Kiek miliimetrų sraigė nučliaužė 2 minutę?"))

keliasMiliimetrais= s12+s22+(s11+s21)*10


centimetrai = keliasMiliimetrais // 10
milimetrai = keliasMiliimetrais % 10
print(f'Sraigė nušliaužė {centimetrai} cm ir {milimetrai} mm kelio')