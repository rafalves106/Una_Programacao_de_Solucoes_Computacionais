"""
Faça um programa que calcule e mostre a tabuada de multiplicação de um número digitado pelo usuário
"""

numeroDaTabuada = int(input("Digite o número da tabuada: "))

multiplicando = 1;

while multiplicando <= 10: 
    print("Veja o número", numeroDaTabuada, "vezes", multiplicando, "é igual a:", numeroDaTabuada * multiplicando)
    multiplicando += 1