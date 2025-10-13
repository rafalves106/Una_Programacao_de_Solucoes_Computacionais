"""
4. Faça um programa que leia dois números inteiros e que imprima todos os
números inteiros existentes entre o menor e o maior número informados.
"""

num_1 = int(input("Digite o primeiro número inteiro: "))
num_2 = int(input("Digite o segundo número inteiro: "))

maior = 0
menor = 0

if num_1 > num_2:
    maior = num_1
    menor = num_2
elif num_1 < num_2:
    menor = num_1
    maior = num_2
else:
    print("Os números são iguais, não há números inteiros entre eles.")

if maior:
    for i in range(menor + 1, maior):
        print(i, "está entre", menor, "e", maior)