txt = 'Mano batai buvo du. Prisigeriau - nerandu'
print(len(txt))

raideA = txt.count('a')
print(raideA)

print(txt.capitalize()) # pirma raide pakelia

print(txt.upper())
print(txt.lower())
print(txt.isupper()) # 'Ar visos didziosios?'
print(txt.islower()) # 'Ar visos mazosios?'

print(txt.find('a'))
print(txt.find('a', txt.find('a')+1))
print(txt.find('a', 8, 15)) # ras tarp 8 ir 15 simboliu

print(txt.rfind('a'))