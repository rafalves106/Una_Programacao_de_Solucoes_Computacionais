"""
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
"""

salarioAtual = float(input("Digite seu salário atual: "))
aumento = 25.0;

valorDoAumento = (aumento * salarioAtual) / 100;
salarioNovo = salarioAtual + valorDoAumento;

print("Seu salário atual R$",  salarioAtual, "após o aumento de", aumento, "%", "agora vale R$", salarioNovo)