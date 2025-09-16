"""
8. Faça um programa que leia o sexo e a altura (H - em metros) de uma
pessoa, calcule e apresente seu peso ideal utilizando as seguintes fórmulas:
Peso ideal (homens) = (72,7 * H) – 58.
Peso ideal (mulheres) = (62,1 * H) – 44,7
Sugestão: para identificar o sexo da pessoa, solicite ao usuário que informe
1 para homens, e 2 para mulheres
"""

altura = float(input("Digite a altura da pessoa em metros (Ex: 1.70): "))
sexo = input("Digite o sexo da pessoa (M/F): ")

peso_ideal_masc = (72.7 * altura) - 58
peso_ideal_fem = (62.1 * altura) - 44.7

if sexo.lower() == "m":
    print("O peso ideal do homem é: %.2fkg" % peso_ideal_masc)
else:
    print("O peso ideal da mulher é: %.2fkg" % peso_ideal_fem)