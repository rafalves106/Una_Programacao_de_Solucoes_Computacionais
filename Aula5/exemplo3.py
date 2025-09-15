"""
Faça um algoritmo que receba dois números e mostre o maior e o menor.

ALGORITMO
DECLARE num1, num2 NUMÉRICO
ESCREVA "Entre com os dois números"
LEIA num1, num2
SE num1 > num2 ENTÃO 
INICIO
	ESCREVA "O maior é ", num1
	ESCREVA "O menor é ", num2
FIM
SENÃO SE num2 > num1 ENTÃO 
INICIO
	ESCREVA "O maior é ", num2
	ESCREVA "O menor é ", num1
FIM
SENÃO 
	ESCREVA "Os dois números são iguais"
FIM_ALGORITMO 
"""

print("Entre com dois números!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))

if num1 > num2:
    print("O maior número é:", num1)
    print("O menor é:", num2)
elif num2 > num1:
    print("O maior número é:", num2)
    print("O menor é:", num1)
else:
    print("Os dois números são iguais.")