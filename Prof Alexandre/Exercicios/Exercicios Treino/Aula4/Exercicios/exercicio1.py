"""
1. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom. Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta.
"""

valorGasto = float(input("Qual o valor gasto pelo cliente: "))
gorjeta = (valorGasto * 10) / 100

print("O valor a ser pago de gorjeta é %.2f" % gorjeta)