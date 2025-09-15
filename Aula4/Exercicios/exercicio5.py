"""
Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
Peso ideal (P) = (72,7 * H) – 58.
"""

resposta = input("Deseja calcular o peso ideal de um homem? (Sim/Não)")
escolha = (resposta.lower() == "sim") or (resposta.lower() == "s")

while escolha:
    user_altura = float(input("Digite a altura em metros para saber o peso ideal: "))
    peso_ideal = (72.7 * user_altura) - 58

    print("O seu peso ideal é: %.2f" % peso_ideal, "Kg.")
    
    resposta = input("Você deseja calcular outro peso ideal? (Sim/Não)")
    escolha = (resposta.lower() == "sim") or (resposta.lower() == "s")

print("Obrigado.")