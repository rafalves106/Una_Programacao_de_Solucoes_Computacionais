"""
2. Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado.
"""

numInt = int(input("Digite um número inteiro e saiba seu antecessor, sucessor, dobro e a metade: "))

numAnt = numInt - 1;
numSuc = numInt + 1;
numDouble = numInt * 2;
numHalf = numInt / 2;

print("O antecessor é", numAnt, ", o sucessor é", numSuc, ", o dobro é", numDouble, ", a metade é", numHalf)