"""
7. Faça um programa que receba 2 números e mostre o seguinte menu:

1 - Somar os dois números
2 - Multiplicar os dois números
3 - Subtrair o número maior pelo número menor (se os dois forem iguais, retorne zero)
4 - Dividir o primeiro número pelo segundo (lembre-se de que não existe divisão por zero)

De acordo com a opção escolhida, exiba o resultado correspondente.
"""

resposta = input("Deseja realizar um cálculo? (Sim/Não) ")

while resposta.lower() == "sim":
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    
    print("Menu de opções:")
    print("1 - Somar os dois números")
    print("2 - Multiplicar os dois números")
    print("3 - Subtrair o número maior pelo número menor")
    print("4 - Dividir o primeiro número pelo segundo")
    
    selecao = input("Escolha uma opção ( 1 / 2 / 3 / 4 ): ")
    
    while selecao not in ["1", "2", "3", "4"]:
        print("Opção inválida. Por favor, escolha uma das opções: ")
        selecao = input("Escolha uma opção ( 1 / 2 / 3 / 4 ): ")
        
    if selecao == "1":
        print("Resultado:", num_1 + num_2)
        
    elif selecao == "2":
        print("Resultado:", num_1 * num_2)
        
    elif selecao == "3":
        if num_1 == num_2:
            print("Resultado é zero. ")
        elif num_1 > num_2:
            print("Resultado:", num_1 - num_2)
        else:
            print("Resultado:", num_2 - num_1)

    elif selecao == "4":
        if num_2 == 0:
            print("Não é possível realizar uma divisão por 0")
        else:
            print("Resultado:", num_1 / num_2)

    resposta = input("Deseja realizar outro cálculo (Sim/Não) ")
        
print("Obrigado! ")