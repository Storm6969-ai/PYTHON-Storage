t1 = 'labai'
t2 = 'noriu'
t3 = 'namo'
t4 = t1 + ' ' + t2 + ' ' + t3 # naudoja daug resursu
print(t4)

t5 = '%s %s %s'%(t1, t2, t3)
print(t5)

t6 = '{} {} {}'.format(t3, t2, t1)
print(t6)

t7 = f'{t3} {t1} {t2}'
print(t7)