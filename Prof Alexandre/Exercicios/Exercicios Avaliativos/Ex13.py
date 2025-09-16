"""
13. Faça um programa que leia o um número inteiro entre 1 e 7 e escreva o
dia da semana correspondente. Caso o usuário digite um número fora desse
intervalo, deverá aparecer uma mensagem informando que não existe dia
da semana com esse número.
"""

num = int(input("Digite um número entre 1 e 7: "))

if num >= 1 and num <= 7:
    txt_format = "O dia da semana correspondente ao valor"
    if num == 1:
        print(txt_format, num, "é Segunda-Feira. ")
    elif num == 2:
        print(txt_format, num, "é Terça-Feira. ")
    elif num == 3:
        print(txt_format, num, "é Quarta-Feira. ")
    elif num == 4:
        print(txt_format, num, "é Quinta-Feira. ")
    elif num == 5:
        print(txt_format, num, "é Sexta-Feira. ")
    elif num == 6:
        print(txt_format, num, "é Sábado. ")
    elif num == 7:
        print(txt_format, num, "é Domingo. ")
else:
    print("Não existe dia da semana com esse número.")