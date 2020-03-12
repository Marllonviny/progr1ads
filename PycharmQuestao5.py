# ADS - UNIFIP
# data: 12 de março de 2020
# Marllon Vinicius Alves lucena

valorOriginal = float(input('Qual o valor da divida do devedor ? '))
diasAtrasado = int(input('Quantos dias está em atraso tal divida ? '))
valorMulta = float(input('Qual a multa pelo atraso ? '))
s = valorOriginal + diasAtrasado / valorMulta
print('O valor de %.2f reais com a soma dos %d dias, com a multa de %.2f por dia dá: %2.f' % (valorOriginal, diasAtrasado, valorMulta, s))