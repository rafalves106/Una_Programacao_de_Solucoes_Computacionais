"""
6. Faça um programa que leia um número e que calcule o fatorial deste número.
"""

num = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(num, 1, -1):
    fatorial *= i
    print(fatorial)

print("O fatorial de", num, "é", fatorial)