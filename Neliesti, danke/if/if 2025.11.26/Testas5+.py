suma = float(input('Kokia saskaitos suma (€)...'))
lojalumoKortele = input('Ar turite lojalumo kortele (taip/ne)...')
if lojalumoKortele == 'taip':
    lojalumoKortele = True
else:
    lojalumoKortele = False

if suma>100:
    a = suma*0.85
elif 100>=suma>=50:
    a = suma*0.9
elif 50>suma and lojalumoKortele:
    a = suma*0.95
else:
    a = suma
print(f'Moketi {a}€')