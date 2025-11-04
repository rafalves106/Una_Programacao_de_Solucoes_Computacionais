"""
4. Um número inteiro e que retorne o valor do fatorial deste número
5. Um número inteiro e que retorne a soma dos números pares entre 1 e o número (inclusive)
6. Um número inteiro e positivo, que retorne a soma dos elementos inteiros existentes entre
1 e o número (inclusive)
7. Dois números inteiros e que retorne a multiplicação do primeiro pelo segundo, utilizando
somente operações de soma.
8. Dois números inteiros e que retorne a potência do primeiro elevado ao segundo, utilizando
somente operações de multiplicação.
9. Um número inteiro e que retorne True se o número for par, e False caso contrário
10. Um número inteiro e que retorne True se o número for primo, e False caso contrário
"""

""" 1 - Função que retorna o dobro de um valor calculado no parâmetro x """
def double(x):
    return x * 2

""" 2 - Função que retorna a idade de uma pessoa, recebendo sua data de nascimento e um ano base para realizar o cálculo da idade """
def anoBase(anoNasc, anoBase):
    
    if anoBase < anoNasc:
        calc = "Não é possível realizar o cálculo"
    else:
        calc = anoBase - anoNasc
    return calc

""" 3 - Função que recebe dois números inteiros e calcula o maior deles """
def comparaNum(num_1, num_2):
    maiorNum = 0
    if num_1 > num_2:
        maiorNum = num_1
    elif num_2 > num_1:
        maiorNum = num_2
    else:
        maiorNum = "Os números são iguais"
    
    return maiorNum

""" 4 - Função que recebe um número inteiro e que retorne o valor do fatorial deste número """


x = int(input("Digite um número inteiro: "))
print(double(x))

x = int(input("Digite o ano de nascimento: "))
y = int(input("Digite o ano base: "))
print(anoBase(x, y))

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
print(comparaNum(x,y))