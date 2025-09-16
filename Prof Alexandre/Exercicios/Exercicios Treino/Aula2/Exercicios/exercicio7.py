""""
Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.
"""

salarioMinimo = float(input("Digite o valor atual do salário mínimo no formato (xxxx.xx): "))
salarioAtual = float(input("Digite o valor do seu salário atual no formato (xxxx.xx): "))

calculo = '%.2f' % (salarioAtual / salarioMinimo);

print("Você recebe", calculo, "salários mínimos");