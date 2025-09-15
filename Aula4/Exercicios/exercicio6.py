"""
Faça o mesmo programa do item anterior, utilizando a fórmula para o cálculo do peso ideal para mulheres:
Peso ideal (P) = (62,1 * H) – 44,7
"""

resposta = input("Deseja calcular o peso ideal de uma mulher? (Sim/Não)")
escolha = (resposta.lower() == "sim") or (resposta.lower() == "s")

while escolha:
    user_altura = float(input("Digite a altura em metros para saber o peso ideal: "))
    peso_ideal = (62.1 * user_altura) - 44.7

    print("O seu peso ideal é: %.2f" % peso_ideal, "Kg.")
    
    resposta = input("Você deseja calcular outro peso ideal? (Sim/Não)")
    escolha = (resposta.lower() == "sim") or (resposta.lower() == "s")

print("Obrigado.")