"""
Faça um algoritmo que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
>= 0 e < 3
REPROVADO

>= 3 e < 7
EXAME

>= 7 e <= 10
APROVADO
"""

nota1 = float(input("Digite a sua nota 1: "))
nota2 = float(input("Digite a sua nota 2: "))
nota3 = float(input("Digite a sua nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print("A sua média foi: %.2f" % media)

if media >= 0 and media < 3:
    print("Reprovado. ")
elif media >= 3 and media < 7:
    print("Exame. ")
elif media >= 7 and media <= 10:
    print("Aprovado. ")
else:
    print("Digite suas notas corretamente. ")