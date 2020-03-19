nota1 = float(input('Dê a primeira nota: '))
nota2 = float(input('Dê a segunda nota: '))
media = (nota1 + nota2) /2
print('Tirando %.1f e %.1f , a media do aluno é %.1f' % (nota1, nota2, media))
if 7 > media >= 4:
    print("O aluno esta em recuperação")
elif media < 6:
    print('O aluno está reprovado!')
elif media >= 7:
    print('O aluno foi aprovado!!')
