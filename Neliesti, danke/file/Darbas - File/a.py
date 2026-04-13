from random import randint

kartu = 0

def ivedimas(ivedimoSakymas):
  while True:
    try:
      print()
      ivesta = int(input(ivedimoSakymas))
      if ivesta < 1:
        raise ValueError()
      else:
        return ivesta
    except:
      print("neleistinas lygmuo, bandyk vėl")

def game(kartu):
  
  ivestasSk = ivedimas("Iki kokio skaičiaus ieškoti...  ")
  f.write(f'Vartotojo įrašytas skaičius: {ivestasSk}\n')

  randomSk = randint(1, ivestasSk)
  f.write(f'Sugeneruotas skaičius: {randomSk}\n')

  kelintas = 0
  while True:
    kelintas += 1
    dabartinisSk = ivedimas(f'{kelintas} spėjimas... ')
    f.write(f'{kelintas} spėjimu vartotojas įvedė {dabartinisSk}. ')
    if dabartinisSk == randomSk:
      print("ATSPĖJAI")
      f.write('Tai teisingas atsakymas! \n \n')
      break
    else:
      if dabartinisSk < randomSk:
        print("Skaičius per mažas", end=" || ")
        x = 'didesnis'
      elif dabartinisSk > randomSk:
        print("Skaičius per didelis", end=" || ")
        x = 'mažesnis'
      f.write(f'Sugeneruotas skaičius yra {x}\n')
      print("bandyk vėl")
  print(f'\nPABAIGA\nĮrašytas skaičius: {ivestasSk}\nSugeneruotas skaičius: {randomSk}')
  kartu += 1
  if input('Ar nori žaisti darkart?... ') == 'taip':
    f.write('Žaidėjas žaidžia darkart')
    kartu = game(kartu)
  else:
    f.write('Žaidėjas NEžaidžia darkart')
  f.write('\n\n')
  return kartu


with open('reg.txt', 'w', encoding='utf-8') as f:
  kartu = game(kartu)
  f.write(f'Žaidėjas žaidė {kartu} kart')
