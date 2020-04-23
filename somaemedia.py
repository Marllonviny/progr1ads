contador = 1
temp = 0
soma = 0
media = 0
while contador <= 5:
    temp = int(input('insira um valor: '))
    soma = temp + soma
    contador += 1
media = soma / 5

print(soma)

print(media)
