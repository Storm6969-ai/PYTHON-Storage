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

def game(kartu):
  zaidejas1 = input("Pirmas žaidėjas..."); zaidejas2 = input("Antras žaidėjas...")
  f.write(f'Žaidėjai: {zaidejas1} ir {zaidejas2}\n')

  lazdeliuSk = int(input("Kieki lazdelių..."))
  f.write(f'Lazdelių sk: {lazdeliuSk}\n')

  if randint(1, 2) == 1:
    pirmasEina = zaidejas1; antrasEina = zaidejas2
  else:
    pirmasEina = zaidejas2; antrasEina = zaidejas1
  f.write(f'Žaidimą pradeda: {pirmasEina}\n')

  while(lazdeliuSk > 0):
    while True:
      pirmasPralaimejo = True
      kiekIma = ivedimas(f"Liko {lazdeliuSk} lazdeles. Kiek ima {pirmasEina}?... ")
      lazdeliuSk -= kiekIma
      f.write(f"{pirmasEina} paėma {kiekIma} lazdelių. Liko {lazdeliuSk}\n")
      break

    while True:
      pirmasPralaimejo = False
      kiekIma = ivedimas(f"Liko {lazdeliuSk} lazdeles. Kiek ima {antrasEina}?... ")
      lazdeliuSk -= kiekIma
      f.write(f"{pirmasEina} paėma {kiekIma} lazdelių. Liko {lazdeliuSk}\n")
      break

  if(pirmasPralaimejo):
    print(f"Pralaimėjo {pirmasEina}")
  else:
    print(f"Pralaimėjo {antrasEina}")

  kartu += 1
  if input('Ar nori žaisti darkart?... ') == 'taip':
    f.write('Žaidėjai žaidžia darkart\n\n')
    kartu = game(kartu)
  else:
    f.write('Žaidėjai NEžaidžia darkart\n\n')
  return kartu

kartu = 0

with open('reg.txt', 'w', encoding='utf-8') as f:
  kartu = game(kartu)
  f.write(f'Žaidėjas žaidė {kartu} kart')
