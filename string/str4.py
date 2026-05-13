t = '123ab$#%&465'
print(t.isalnum()) # 'Ar visi skaiciai AR raides?'
t1 = 'Labas'
print(t1.isalpha()) # 'Ar visi raides?'

t3 = '        '
t4 = ''
print(t3.isspace()) 
print(t4.isspace()) 

t5 = ('     tuputis           tarpu    '.strip(' '))
print(t5)
print('     tuputis           tarpu    '.strip())
print('     tuputis           tarpu    '.strip('*'))
print('     tuputis           tarpu    '.strip('* '))

t8 = '    h    '
if t8.strip():
    print('netuscia')
else:
    print("tuscia")

t9 = 'Pirmas kartas'
print(t9.startswith('pir'))
print(t9.startswith('Pir'))
print(t9.endswith('as'))