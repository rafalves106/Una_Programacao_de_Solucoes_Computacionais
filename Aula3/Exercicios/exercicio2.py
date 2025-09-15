"""
Exercícios de fixação
2) FUPQ imprima a soma dos seguintes números: 12 38 145 186 766 941
"""

#Declara variável números como array de números
arrayDeNumeros = [12, 38, 145, 186, 766, 941]

#Declara variável soma vazia
soma = 0;

#Declara variável x vazia
x = 0;

#Estrutura While, onde enquanto x for menor ou igual ao tamanho do array de números o for é lançado
while x <= len(arrayDeNumeros):
    
    #Estrutura For, onde o x para cada número em arrayDeNumeros é adicionado no valor da variável soma, enquanto a condição do while for válida 
    for x in arrayDeNumeros:
        soma += x
    
    #Imprime o texto, concatenando o valor da soma
    print("A soma dos números é", soma)