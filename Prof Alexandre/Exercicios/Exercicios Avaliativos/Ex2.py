"""
2. Peça ao usuário um número. Se ele for menor ou igual zero, ou maior que
100, mostre "Número fora do intervalo".
"""

num = float(input("Digite um número: "))

if num <= 0 or num > 100:
    print("Número fora do intervalo de 1 a 100")
else:
    print("Número dentro do invervalo de 1 a 100")
