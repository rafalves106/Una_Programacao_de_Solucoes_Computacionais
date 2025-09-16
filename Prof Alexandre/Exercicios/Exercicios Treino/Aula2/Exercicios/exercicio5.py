"""
Faça um programa que calcule e mostre a área de um losango AREA = (DIAGONAL MAIOR * DIAGONAL MENOR)/2
"""

diagonalMaior = float(input("Digite o valor da diagonal maior em cm2: "))
diagonalMenor = float(input("Digite o valor da diagonal menor em cm2: "))
area = '%.2f' % ((diagonalMaior * diagonalMenor) / 2)

print("A área do losango é de:", area, "cm2")