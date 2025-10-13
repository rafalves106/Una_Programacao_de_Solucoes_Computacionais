"""
2. Faça um programa que leia um número e que imprima os números ímpares de
1 até o número informado.
"""

num = int(input("Digite a quantidade de números ímpares: "))

print("-------Aqui estão",num,"Números Ímpares-------")
for i in range(1, num * 2, 2):
    print(i)