# Logines operacijos
# "not" --------> neigimas
# "and" --------> logine daugyba  (minus*minus = plus*plus = true, minus*plus = false)
# "or" ---------> logine sudetis

darboDiena = True #teiginys automatiskai "True"
geraSavijauta = False
arEisiuIMokykla = darboDiena and geraSavijauta
print(arEisiuIMokykla)


darboDiena2 = True
geraSavijauta2 = False
arEisiuIMokykla2 = darboDiena2 and not geraSavijauta2 # neigia neigiama elementa
print(arEisiuIMokykla2)


darboDiena3 = True
blogaSavijauta3 = False
arEisiuIMokykla3 = darboDiena3 and not blogaSavijauta3 # neigia elementa
print(arEisiuIMokykla3)