from random import randint

def ivedimas(ivedimoSakymas):
  while True:
    try:
      print()
      ivesta = int(input(ivedimoSakymas))
      if (0 < ivesta < 4):
        return ivesta
      else:
        raise ValueError()
    except:
      print("neleistinas lygmuo, bandyk vėl")



zaidejas1 = input("Pirmas žaidėjas..."); zaidejas2 = input("Antras žaidėjas...")
# f.write(f'Žaidėjai {zaidejas1} ir {zaidejas2}\n')

lazdeliuSk = input("Kieki lazdelių...")
# f.write(f'Lazdelių sk: {lazdeliuSk}')

if randint(1, 2) == 1:
  pirmasEina = zaidejas1; antrasEina = zaidejas2
else:
  pirmasEina = zaidejas2; antrasEina = zaidejas1




while True:
  kiekIma = ivedimas(f"Liko {lazdeliuSk} lazdeles. Kiek ima {pirmasEina}?... ")
  lazdeliuSk -= kiekIma
  kiekIma = ivedimas(f"Liko {lazdeliuSk} lazdeles. Kiek ima {antrasEina}?... ")
  lazdeliuSk -= kiekIma



# with open('reg.txt', 'w', encoding='utf-8') as f:
