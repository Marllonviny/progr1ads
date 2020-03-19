numero1 = int(input(' Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

#Verifique o menor valor

if numero2 < numero1:
    print(numero1)
elif numero1 < numero2:
    print(numero2)
else:
    print('Os numeros são iguais!')
