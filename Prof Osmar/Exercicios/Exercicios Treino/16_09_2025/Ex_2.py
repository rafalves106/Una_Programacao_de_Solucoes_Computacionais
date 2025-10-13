"""
2) Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

Menu de opções:
1. Multiplicar dois números.
2. Dividir dois números.

Faça o programa usando uma estrutura condicional composta.
"""

print("Menu de opções:")
print("1. Multiplicar dois números.")
print("2. Dividir dois números.")

opcao = int(input("Digite a opção desejada do menu (1 ou 2): "))

if opcao == 1:
    mult_1 = float(input("Digite o primeiro número da multiplicação: "))
    mult_2 = float(input("Digite o segundo número da multiplicação: "))
    
    total = mult_1 * mult_2
    print("Este é o total do seu cálculo:", total)
    
elif opcao == 2:
    div_1 = float(input("Digite o primeiro número da divisão: "))
    div_2 = float(input("Digite o segundo número da divisão: "))
    
    if div_2 == 0:
        print("Não existe divisão por zero. ")
    else:
        total = div_1 / div_2
        print("Este é o total do seu cálculo:", total)
else:
    print("Opção não disponível. ")