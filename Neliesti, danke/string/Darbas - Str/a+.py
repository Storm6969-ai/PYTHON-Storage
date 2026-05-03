n = 'abcdefghijklmnopqrstuvwxyz'
with open("reg.txt", "w") as reg:
  with open("duom.txt", "r") as duom:
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