turno = input('Qual turno você estuda?: ')

turnomanha = ('M','manha')

turnotarde = ('V','tarde')

turnonoite = ('N','noite')

if turno in turnomanha:
    print('Bon Jour!')
elif turno in turnotarde:
    print('Buon pomeriggio!')
elif turno in turnonoite:
    print('Bonne nuit!')
else:
    print('vá estudar!')