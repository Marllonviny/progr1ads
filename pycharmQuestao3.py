kminicial = int(input("informe o KM inicial: "))
kmFinal = int(input('informe o KM final:'))
qtdaLitros = float(input("Quantos litros foram gastos no percurso"))
totalKM = kmFinal - kminicial
media = totalKM / qtdaLitros
print('a media de litros que seu veiculo faz é %.f' % media)