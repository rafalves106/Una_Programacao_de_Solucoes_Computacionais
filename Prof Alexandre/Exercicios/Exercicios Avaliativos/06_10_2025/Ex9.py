"""
9. Faça um programa que leia a idade e peso de sete pessoas. Calcule e mostre:
- a quantidade de pessoas com mais de 90 kg
- a média das idades das sete pessoas
- a menor e a maior idade
"""

maiorIdade = 0
menorIdade = 200
somaIdades = 0
contadorPeso = 0

for i in range(7):
    idade = int(input("Informe a idade de uma pessoa: "))
    peso = float(input("Informe o peso de uma pessoa em kg: "))
    
    if peso > 90:
        contadorPeso += 1
    
    if idade >= maiorIdade:
        maiorIdade = idade
    elif idade <= menorIdade:
        menorIdade = idade
        
    somaIdades += idade
    
mediaIdades = somaIdades / 7
    
print("Quantidade de pessoas com mais de 90kg é", contadorPeso)
print("A média de idades foi: %.0f" % mediaIdades)
print("O maior idade recebida foi de:", maiorIdade)
print("A menor idade recebida foi de:", menorIdade)