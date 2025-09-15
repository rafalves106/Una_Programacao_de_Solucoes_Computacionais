"""
Faça um algoritmo que receba dois números e mostre a diferença entre o primeiro e o segundo número. Se a diferença for negativa, emita uma mensagem informando que o segundo é maior que o primeiro

ALGORITMO
	DECLARE n1, n2, dif NUMÉRICO
	ESCREVA "Entre com os dois números"
	LEIA n1, n2
	dif ← n1 - n2
	ESCREVA "A diferença entre os números é ", dif
	SE dif < 0 ENTÃO 
	ESCREVA "A diferença é negativa porque o segundo é maior que o primeiro"
    FIM_ALGORITMO 
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

dif = n1 - n2

print("A diferença entre os números é:", dif)

if dif < 0:
    print("A diferença é negativa porque o segundo é maior que o primeiro.")
