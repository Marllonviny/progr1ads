numero1 = int(input('Digite o valor da mercadoria: '))
numero2 = int(input('Digite o valor da segunda mercadoria: '))

if numero1 > numero2:
    print('Você deve comprar o produto com o valor de %d ' % numero2)
elif numero2 > numero1:
    print('Compre o produto com o valor %d' % numero1)
else:
    print('Não compre nada que ta caro!')

