"""
12. Faça um programa que leia dois números inteiros e que calcule a potência do
primeiro elevado ao segundo, utilizando somente operações de multiplicação.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))

resultado = 1
for i in range(1, num_2 + 1, 1):
    resultado *= num_1

print(resultado)