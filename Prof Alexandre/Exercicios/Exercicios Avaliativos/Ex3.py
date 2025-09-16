"""
3. Faça um programa que solicite um número inteiro. Mostre uma
mensagem informando se o número é par ou ímpar.
"""

int_num = int(input("Digite um número inteiro para saber se é par ou ímpar: "))

if int_num % 2 == 0:
    print(int_num, "é par.")
else:
    print(int_num, "é ímpar.")