"""
11. Faça um programa que receba a idade de um nadador e mostre a sua
categoria
IDADE CATEGORIA
até 7 anos INFANTIL
8 a 10 anos JUVENIL
11 a 15 anos ADOLESCENTE
16 a 30 anos ADULTO
acima de 30 anos SENIOR
"""

swimmer_age = int(input("Digite a idade do nadador: "))
text = "O nadador pertence a categoria: "

if swimmer_age <= 7:
    print(text + "INFANTIL")
elif swimmer_age >= 8 and swimmer_age <= 10:
    print(text + "JUVENIL")
elif swimmer_age >= 11 and swimmer_age <= 15:
    print(text + "ADOLESCENTE")
elif swimmer_age >= 16 and swimmer_age <= 30:
    print(text + "ADULTO")
else:
    print(text + "SENIOR")