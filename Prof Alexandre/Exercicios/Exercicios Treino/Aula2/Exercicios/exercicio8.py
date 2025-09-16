""""
8. Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) O seu novo peso, se a pessoa engordar 15% sobre o peso digitado
b) O seu novo peso, se a pessoa emagrecer 20% sobre o peso digitado
"""

pesoAtual = float(input("Digite o seu peso atual: "))
kgEngordados = (pesoAtual * 15) / 100
kgEmagrecidos = (pesoAtual * 20) / 100

aposEngordar = pesoAtual + kgEngordados;
aposEmagrecer = pesoAtual - kgEmagrecidos;

print("Seu peso depois de engordar 15%:", aposEngordar, "kg")
print("Seu peso depois de emagrecer 20%:", aposEmagrecer, "kg")