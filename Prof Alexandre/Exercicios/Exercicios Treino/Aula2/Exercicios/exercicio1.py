"""
Faça um programa que receba três notas, calcule e mostre a média aritmética entre elas.
"""

n1 = int(input("Digite a primeira nota: "));
n2 = int(input("Digite a segunda nota: "));
n3 = int(input("Digite a terceira nota: "));

soma = n1 + n2 + n3;
media = soma / 3

print("A média das notas é: %.2f" % media)