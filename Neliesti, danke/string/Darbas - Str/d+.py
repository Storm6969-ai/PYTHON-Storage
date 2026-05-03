with open("duom4.txt", "r", encoding='utf-8') as duom:
  stuff = duom.read()

upper = 2; lower = 2; num = 2; special = 2
with open("reg4.txt", "w", encoding='utf-8') as reg:
  for i in stuff:

    if i.isupper():
      upper -= 1
    elif i.islower():
      lower -= 1

    if i in '0123456789':
      num -= 1
    
    if i in '!#$%^&*()?+-/,.':
      special -= 1

  if len(stuff) < 12:
    reg.write('Netinka. Trūksta simbolių')
  elif upper > 0:
    reg.write('Netinka. Trūksta didžiųjų raidžių')
  elif lower > 0:
    reg.write('Netinka. Trūksta mažųjų raidžių')
  elif num > 0:
    reg.write('Netinka. Trūksta skaitmenų')
  elif special > 0:
    reg.write('Netinka. Trūksta specialiųjų simbolių')