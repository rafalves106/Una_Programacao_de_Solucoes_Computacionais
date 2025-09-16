"""
5. Faça um programa que receba as duas notas de um aluno, calcule sua
média, e que imprima a sua situação:
>= 7 -> Aprovado
< 7 -> Reprovado
"""

nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print("O aluno foi aprovado com a média de: %.2f" % media)
else:
    print("O aluno foi reprovado com a média de: %.2f" % media)