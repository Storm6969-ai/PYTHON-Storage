n = 'aąbcdeęėfghiįyjklmnoprsštuųūvzž'
with open("reg2.txt", "w", encoding="utf-8") as reg:
  with open("duom2.txt", "r", encoding="utf-8") as duom:
    stuff = duom.read()
  for i in stuff:
    if i.lower() in n:
      newi = n[len(n) -1 - n.find(i.lower())]
      if i.isupper():
        newi = newi.upper()
      else:
        newi = newi.lower()
    else:
      newi = i
    reg.write(newi)