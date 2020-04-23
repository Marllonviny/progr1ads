login = str(input('Digite seu login: ')).upper()
senha = str(input('Digite sua senha: ')).upper()

while login == senha:
    print('Senha Invalida, Digite novamente!')
    senha = str(input('Digite a senha novamente: ').upper())

print('Congratulations!')

