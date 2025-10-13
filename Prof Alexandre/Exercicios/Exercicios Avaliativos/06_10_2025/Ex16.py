"""
4. Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos
A leitura será encerrada quando o usuário informar uma idade negativa
"""

idade = int(input("Digite a idade de uma pessoa: "))
contador = 1
contador_cinquenta = 0
contador_quarenta = 0
soma_idades = 0

while idade >= 0:
    contador += 1
    soma_idades += idade
    
    if idade > 50:
        contador_cinquenta += 1
    elif idade < 40:
        contador_quarenta += 1
        
    idade = int(input("Digite a idade de uma outra pessoa: "))

media = soma_idades / contador
percentual_40anos = (contador_quarenta / contador) * 100

print(contador_cinquenta, "pessoas possuem mais de 50 anos.")
print("A idade média das pessoas foi de %.0f" % media, "anos.")
print("%.2f" % percentual_40anos, "% das pessoas possuem menos de 40 anos.")
