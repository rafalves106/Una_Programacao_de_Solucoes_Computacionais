"""
Faça um programa que receba a cotação do dólar em reais, e um valor que o usuário possui em dólares. Imprima este valor em reais.
"""

cotacaoDolar = 5.65

valorEmReais = float(input("Digite a sua quantidade de R$ na carteira: "));
conversor = '%.2f' % (valorEmReais / cotacaoDolar);

print("Você tem um total de $" + conversor)