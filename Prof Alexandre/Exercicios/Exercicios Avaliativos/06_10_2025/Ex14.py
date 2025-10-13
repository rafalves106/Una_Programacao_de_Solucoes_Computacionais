"""
2. Escreva um programa que fique pedindo números positivos ao usuário e que
mostre a soma de todos eles. O programa irá terminar quando o usuário digitar
um número negativo.
"""

num = int(input("Digite um número positivo: "))
soma = 0

while num >= 0:
    soma += num
    num = int(input("Digite outro número positivo: "))

print("A soma total foi de:", soma)
print("FIM DO PROGRAMA!")