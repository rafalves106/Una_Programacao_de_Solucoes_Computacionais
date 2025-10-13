"""
5. Faça um programa que leia um número que calcule a soma dos números
inteiros entre 1 e o número informado.
"""

num = int(input("Digite um número inteiro: "))
    
soma = 0
for i in range(1, num):
    soma += i
    print(soma)