# Questão 2 - litros cubicos de agua
# Marllon Vinicius
tempo = int(input('quanto tempo demora seu banho? '))
litros = 9
gasto = tempo * litros
qtda = 1000 / gasto
print('Se você passar %d minutos no banho, você conseguirá %d banho(s) nesse mesmo tempo' % (tempo, qtda))