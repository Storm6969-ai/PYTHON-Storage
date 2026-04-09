vid = float(input('Mokinio vidurkis....'))
lank = float(input('Mokinio lankomumas (%)....'))

if vid>=9 and lank>=90:
    print('Padidinta stipendija')
elif vid>=7 and lank>=75:
    print('Paprasta stipendija')
elif vid<7 and lank<60:
    print('Stipendija neskiriama')
else:
    print('Reikia komisijos sprendimo')