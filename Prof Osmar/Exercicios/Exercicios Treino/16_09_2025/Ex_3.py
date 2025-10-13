"""
3) Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as
regras a seguir. Para idade inferior a 5, deverá mostrar uma mensagem dizendo que o
nadador não se enquadra em nenhuma categoria.
- Infantil: de 5 a 7 anos
- Juvenil: de 8 a 10 anos
- Adolescente: de 11 a 15 anos
- Adulto: de 16 a 30 anos
- Sênior: acima de 30 anos
"""

swimmer_age = int(input("Digite a idade do nadador em anos: "))

if swimmer_age >= 1 and swimmer_age <=120:
    if swimmer_age >= 5 and swimmer_age <= 7:
        print("O nadador se enquadra na categoria infantil. ")
    elif swimmer_age >= 8 and swimmer_age <= 10:
        print("O nadador se enquadra na categoria juvenil. ")
    elif swimmer_age >= 11 and swimmer_age <= 15:
        print("O nadador se enquadra na categoria adolescente. ")
    elif swimmer_age >= 16 and swimmer_age <= 30:
        print("O nadador se enquadra na categoria adulto. ")
    elif swimmer_age > 30:
        print("O nadador se enquadra na categoria sênior. ")
    else:
        print("O nadador não se enquadra em nenhuma categoria. ")
else:
    print("Idade inválida. ")