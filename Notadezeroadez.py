nota = float(input('Digite uma nota: '))

while nota < 0 or nota > 10:
    print('Repita a operação')
    nota = float(input('Digite uma nota: '))
    if nota >= 0 and nota <= 10:

        print('Muito bem!')