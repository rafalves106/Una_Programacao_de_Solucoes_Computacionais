"""
8. Faça um programa que leia o sexo e o peso de 10 pessoas, e mostre quantas
pessoas do sexo masculino possuem peso entre 60 e 80 kg, bem como a
quantidade de mulheres que possuem peso entre 50 e 70 kg.
"""

contadorMasculino = 0
contadorFeminino = 0

for i in range(10):
    sexo = input("Informe o sexo da pessoa (m/f): ")
    peso = float(input("Informe o peso de uma pessoa em kg: "))
    
    if sexo == "m" and peso >= 60 and peso <= 80:
        contadorMasculino += 1
    elif sexo == "f" and peso >= 50 and peso <= 70:
        contadorFeminino += 1

print("A quantidade de homens que possuem entre 60kg e 80kg é", contadorMasculino)
print("A quantidade de mulheres que possuem entre 50kg e 70kg é", contadorFeminino)