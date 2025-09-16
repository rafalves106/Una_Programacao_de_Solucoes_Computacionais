"""
13. Faça um programa que leia o um número inteiro entre 1 e 7 e escreva o
dia da semana correspondente. Caso o usuário digite um número fora desse
intervalo, deverá aparecer uma mensagem informando que não existe dia
da semana com esse número.
"""

num = int(input("Digite um número entre 1 e 7: "))

if num >= 1 and num <= 7:
    dias_semana = ("Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo")
    txt_format = " corresponde ao valor"
    print(dias_semana[num - 1] + txt_format, num)
else:
    print("Não existe dia da semana com esse número.")