"""
Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
		>= 7 -> Aprovado
		< 7 -> Reprovado
"""

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2
print("A média foi: %.2f" % media)

if media >= 7:
    print("Você foi aprovado! ")
elif media < 7:
    print("Você foi reprovado! ")
else:
    print("Insira as notas corretamente. ")
