nota1 = float(input('Dê a primeira nota: '))
nota2 = float(input('Dê a segunda nota: '))
media = (nota1 + nota2) /2


if media > 0 and media <=4.0:
    print('Media: %.1f, Conceito: E.' % (media))
elif media > 4.0 and media <= 6.0:
    print('Media: %.1f, Conceito: D.' % (media))
elif media > 6.0 and media <= 7.5:
    print('Media: %1.f, Conceito: C.' % (media))
elif media > 7.5 and media < 9.0:
    print('Media: %1.f, Conceito: B.' % (media))
elif media > 9.0 and media <= 10.0:
    print('Media: %1.f, Conceito: A.' % (media))
else:
    print('Nota inválida, nota: %1.f, nota: %1.f' % (nota1, nota2))