"""
Exercícios de fixação
5) FUPQ receba o nome completo de uma pessoa e a sua idade. Imprima a idade da pessoa seguida de um hífen e o nome da pessoa. 
"""

#Declara variável nomeCompleto e lê a resposta como uma string
nomeCompleto = str(input("Digite o seu nome completo: "))

#Declara variável idade e lê a resposta como um inteiro
idade = int(input("Digite sua idade: "))

#Imprime os textos, concatenando as variaveis idade e nomeCompleto
print("Sua idade é:", idade, "-", nomeCompleto)