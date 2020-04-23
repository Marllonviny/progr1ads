contador = 1
numero = 0
temp = 0

while contador <= 5:
    temp = int(input('Digite um valor: '))
    if temp > numero:
        numero = temp
    contador += 1
print('o maior valor foi %d' % numero)
