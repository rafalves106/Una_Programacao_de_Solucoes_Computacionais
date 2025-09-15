"""
Exercícios de fixação
3) FUQP imprima a média aritmética dos números: 12 38 145 186 766 941
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
    
    #Declara variável mediaAritmetica com valor de soma divido pela quantidade de itens no arrayDeNumeros
    mediaAritmetica = soma / len(arrayDeNumeros)
    
    #Imprime o texto, concatenando o valor da mediaAritmetica
    print("A média aritmetica dos números é:", mediaAritmetica)