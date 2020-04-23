paisA = int(input('Digite a quantidade de habitantes do pais A: '))
paisB = int(input('Digite a quantidade de habitantes do pais B: '))
taxaA = float(input('Insira a porcentagem da taxa de crescimento do Pais A: '))
taxaB = float(input('Insira a porcentagem da taxa de crescimento do Pais B: '))
ano = 0
while paisA <= 1 or paisB <= 1 or taxaA <= 0 or taxaB <= 0 or taxaA <= taxaB and paisA < paisB or taxaB <= taxaA and paisB < paisA:
    print('Algo de errado não está certo')
    if paisA <= 1:
        paisA = int(input('Digite a quantidade de habitantes do pais A: '))
    if paisB <= 1:
        paisB = int(input('Digite a quantidade de habitantes do pais B: '))
    if taxaA <= 0:
        taxaA = float(input('Insira a porcentagem da taxa de crescimento do Pais A: '))
    if taxaB <= 0:
        taxaB = float(input('Insira a porcentagem da taxa de crescimento do Pais B: '))
    if taxaA <= taxaB and paisA < paisB:
        paisA = int(input('Digite a quantidade de habitantes do pais A: '))
        paisB = int(input('Digite a quantidade de habitantes do pais B: '))
        taxaA = float(input('Insira a porcentagem da taxa de crescimento do Pais A: '))
        taxaB = float(input('Insira a porcentagem da taxa de crescimento do Pais B: '))
    if taxaB <= taxaA and paisB < paisA:
        paisA = int(input('Digite a quantidade de habitantes do pais A: '))
        paisB = int(input('Digite a quantidade de habitantes do pais B: '))
        taxaA = float(input('Insira a porcentagem da taxa de crescimento do Pais A: '))
        taxaB = float(input('Insira a porcentagem da taxa de crescimento do Pais B: '))

while paisA < paisB:
    paisA = paisA * (1 + taxaA / 100)
    paisB = paisB * (1 + taxaB / 100)
    ano = ano + 1
    print(paisA)
    print(paisB)
    print(ano)
print('Passaram %s anos' % ano)
