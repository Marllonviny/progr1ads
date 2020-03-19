ano = int(input('Qual o ano que você quer ter uma analise?: '))
if ano % 4 ==0:
    print('O ano %d é bissexto' % ano)
else:
    print('O ano %d não é bissexto' % ano)