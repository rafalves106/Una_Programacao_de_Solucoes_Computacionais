"""
Considerando uma eleição de apenas dois candidatos, faça um programa que leia o número total de eleitores, o número de votos do primeiro candidato e o número de votos do segundo candidato. Em seguida, o programa deverá apresentar o percentual de votos de cada um dos candidatos e o percentual de votos nulos.
"""

votos_candidato1 = int(input("Qual a quantidade de votos que o canditato 1 recebeu? "))
votos_candidato2 = int(input("Qual a quantidade de votos que o canditato 2 recebeu? "))

percentual_candidatos = [((votos_candidato1 / (votos_candidato1 + votos_candidato2)) * 100), ((votos_candidato2 / (votos_candidato1 + votos_candidato2)) * 100)]

print("Percentual do candidato 1: %.2f" % percentual_candidatos[0], "%")
print("Percentual do candidato 2: %.2f" % percentual_candidatos[1], "%")