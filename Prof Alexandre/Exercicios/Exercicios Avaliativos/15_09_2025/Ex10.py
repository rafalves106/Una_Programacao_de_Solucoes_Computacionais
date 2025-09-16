"""
10. Uma empresa decide dar aumento de 30% aos funcionários com salários
inferiores a R$1000,00. Faça um programa que receba o salário do
funcionário e mostre o valor do salário reajustado ou uma mensagem, caso
o funcionário não tenha direito ao aumento.
"""

salario = float(input("Digite o salário do funcionário: "))

if salario >= 1000:
    print("Sem aumento disponível para o funcionário. ")
else:
    aumento = salario * 0.3
    salario += aumento
    print("Novo salário do funcionário é R$ %.2f" % salario)