nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media > 7 and media <= 9:
    print('O aluno foi aprovado! com a nota: %.1f' % (media))
elif media < 7:
    print('O aluno foi reprovado com a media: %.1f' %(media))
elif media == 10:
    print('O aluno foi aprovado com distinção! com a media: %.1f' % (media))