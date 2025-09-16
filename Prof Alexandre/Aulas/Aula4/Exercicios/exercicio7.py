"""
Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7.
"""

a = input("Digite o valor de 'A': ")
b = input("Digite o valor de 'B': ")

a,b = b,a

print("Novo valor de 'A':", a)
print("Novo valor de 'B':", b)