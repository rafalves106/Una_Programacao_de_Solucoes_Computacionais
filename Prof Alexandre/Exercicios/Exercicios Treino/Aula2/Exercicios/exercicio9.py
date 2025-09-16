import math

"""
Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
"""

catetoA = float(input("Digite o valor do cateto a: "))
catetoB = float(input("Digite o valor do cateto b: "))

calculoHipotenusa = ((catetoA * catetoA) + (catetoB * catetoB))

hipotenusa = math.sqrt(calculoHipotenusa)

print("O valor da hipotenusa é:", hipotenusa)