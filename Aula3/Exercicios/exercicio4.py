"""
Exercícios de fixação
4) FUPQ receba dois números inteiros e imprima a soma e a subtração do primeiro pelo segundo número
"""

#Declara variável num1 e lê a resposta como um inteiro
num1 = int(input("Digite um número: "))

#Declara variável num2 e lê a resposta como um inteiro
num2 = int(input("Digite outro número: "))

#Declara variável soma, com valor de num1 mais num2
soma = num1 + num2;

#Declara variável subtração, com valor de num1 menos num2
subtracao = num1 - num2;

#Imprime os textos, concatenando as variaveis soma e subtração
print("A soma entre os números é:", soma, "e a subtração do números é:", subtracao)