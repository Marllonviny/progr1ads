nome = input('Digite um nome: ')
idade = int(input('Digite sua idade: '))
salario = int(input('Digite seu salario: '))
sexo = input('Insira seu sexo: ')
ec = input('Digite seu estado civil: ')
while len(nome) <= 3 or idade < 0 or idade > 150 or salario < 0 or sexo != 'f' and sexo != 'm' or ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    if len(nome) <= 3:
        print('nome invalido')
        nome = input('Digite um nome:')
    if idade < 0 or idade > 150:
        print('idade invalida')
        idade = int(input('Digite sua idade: '))
    if salario < 0:
        print('Tu é pobre misera?')
        salario = int(input('Insira seu salario denovo: '))
    if sexo != 'f' and sexo != 'm':
        print('insira seu sexo com f ou m!')
        sexo = input('Digite seu sexo: ')
    if ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
        print('Insira seu estado civil com s ou c ou v ou d!')
        ec = input('Insira seu estado civil da forma correta: ')
