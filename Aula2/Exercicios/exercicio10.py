import math

"""
Faça um programa que receba o raio, calcule e mostre:
O comprimento de uma esfera (C = 2 *  π  * R)
A área de uma esfera (A = π * R2)
O volume de uma esfera (V = ¾ *  π  * R3)
"""

raio = float(input("Digite o raio em cm: "))
comprimento = 2 * math.pi * raio
area = 4 * math.pi * (raio ** 2)
volume = (4/3) * math.pi * (raio ** 3) 

print("O comprimento da esfera é: %.2f cm" % comprimento)

print("A área da esfera é: %.2f cm2" % area)

print("O volume da esfera é: %.2f cm3" % volume)