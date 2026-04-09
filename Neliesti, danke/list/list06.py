x = [8, 3, 5, 9, 7, 3, 6, 5, 3, 3, 3, 4, 2]

x.append(-8) 
print(x)

x.insert(2, -1000) # '.insert(n, z)' ideda z į n vieta
print(x)

print(x.count(-8)) # '.count(n)' suskaiciuoja kiek yra n

kazkas = x.pop() # isema paskutini elemnta
print(x)

print(kazkas)

x.remove(-1000) # '.remove(n)' pasalina n elemntus
print(x)

del x[0] # del istrina toj vietoj esanti elemnta
print(x)

print(x.index(3, (x.index(3)+1))) # '.index(n, z)' randa numeri n nuo tasko z (z DEAFULT yra 0)


a = [1, 2, 3, 5, 6,] # 'a[x:y:z]' - x - start, y - stop, z - step
print(a[1:3:2])