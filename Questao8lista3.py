produto1 = float(input('Informe o valor do primeiro produto: '))
produto2 = float(input('informe o valor do segundo produto: '))
produto3 = float(input('Informe o valor do terceiro produto: '))


if produto1 < produto2 < produto3:
    print('O produto mais barato é o primeiro produto com o valor de %.2f' % produto1)
elif produto2 < produto1 < produto3:
    print('O produto mais barato é o segundo produto com o valor de %.2f' % produto2)
elif produto3 < produto2 < produto1:
    print('O produto mais barato é o terceiro produto com o valor de %.2f' % produto3)
    