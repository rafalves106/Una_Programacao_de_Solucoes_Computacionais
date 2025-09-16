"""
6. Faça um programa que receba 3 notas de um aluno, calcule e mostre uma
mensagem de acordo com sua média:

MÉDIA MENSAGEM
>= 0 e < 3 REPROVADO
>= 3 e < 7 EXAME
>= 7 e <= 10 APROVADO
"""

nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
nota_3 = float(input("Digite a terceira nota do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 0 and media < 3:
    print("O aluno foi reprovado com a média %.2f" % media)
elif media >= 3 and media < 7:
    print("O aluno com a média %.2f deverá fazer exame." % media)
elif media >= 7 and media <= 10:
    print("O aluno foi aprovado com a média %.2f" % media)
else:
    print("A média %.2f está incorreta, digite novamente as notas." % media)