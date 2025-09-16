"""
4. Faça um programa que receba dois números e mostre o maior e o menor.
Emita uma mensagem, caso os dois sejam iguais.
"""

print("Vamos descobrir o maior entre dois números. ")
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))

if num_1 > num_2:
    print("O primeiro número:", num_1, "é maior que o segundo número:", num_2)
elif num_1 == num_2:
    print("Os números tem o mesmo valor. ")
else:
    print("O segundo número:", num_2, "é maior que o primeiro número:", num_1)