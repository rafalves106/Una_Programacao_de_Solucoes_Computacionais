"""
2. Faça um algoritmo que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
		>= 7 -> Aprovado
		< 7 -> Reprovado

ALGORITMO
DECLARE nota1, nota2, media NUMÉRICO
LEIA nota1, nota2
media ← (nota1 + nota2)/2
SE media >= 7 ENTÃO 
	ESCREVA “APROVADO“
SENÃO 
	ESCREVA “REPROVADO”
FIM_ALGORITMO 
"""

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
media = float

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")