"""
7. Faça um programa que solicite ao usuário que informe o peso, em kg, de 10
pessoas, e em seguida, exiba a média desses pesos.
"""
totalPeso = 0

for i in range(10):
    peso = float(input("Informe o peso de uma pessoa em kg: "))
    totalPeso += peso

mediaDePeso = totalPeso / 10
print("A média dos pesos das pessoas é", mediaDePeso, "kg")