"""
11. Faça um programa que leia dois números inteiros e que calcule a
multiplicação do primeiro pelo segundo, utilizando somente operações de soma.
"""

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))

resultado = 0
for i in range(1, num_2 + 1, 1):
    resultado += num_1

print(resultado)