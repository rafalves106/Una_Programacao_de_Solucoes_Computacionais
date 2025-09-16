"""
Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit (F = (C*1,8) + 32)
"""

tempEmC = float(input("Digite a temperatura em Cº: "))
tempEmF = '%.2f' % ((tempEmC * 1.8) + 32)

print("A temperatura de:", tempEmC, "Cº, em Fahrenheit equivale a", tempEmF, "Fº")