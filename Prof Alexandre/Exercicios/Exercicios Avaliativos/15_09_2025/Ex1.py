"""
1. Peça ao usuário um número. Se ele estiver entre 1 e 100 (inclusive),
mostre "Número dentro do intervalo".
"""

num = float(input("Digite um número: "))

if (num >= 1 and num <= 100):
    print("O número", num, "está entre 1 e 100.")
else:
    print("Não está entre 1 e 100.")