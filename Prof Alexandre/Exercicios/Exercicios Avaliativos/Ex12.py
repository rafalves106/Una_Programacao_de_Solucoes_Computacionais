"""
12. Faça um programa que leia a idade de uma pessoa e informe a sua classe
eleitoral:
- não eleitor (abaixo de 16 anos);
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive)
"""

user_age = int(input("Digite a idade para consulta: "))

if user_age < 16:
    print("Usuário não eleitor. ")
elif (user_age >= 16 and user_age < 18) or (user_age >= 65):
    print("Usuário é eleitor facultativo. ")
elif user_age >= 18 and user_age < 65:
    print("Usuário é eleitor obrigatório. ")