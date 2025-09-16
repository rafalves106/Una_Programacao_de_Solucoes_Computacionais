"""
4. Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa
Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
IMC= PESO/ALTURA2
e, a situação do peso é determinada pela tabela ao lado:

IMC abaixo de 20
Abaixo do peso

IMC de 20 até 25
Peso Normal

IMC de 25 até 30
Sobre Peso

IMC de 30 até 40
Obeso

IMC de 40 e acima
Obeso Mórbido
"""
import math

peso_user = float(input("Digite o seu peso atual em quilos: "))
altura_user = float(input("Digite a sua altura em metros: "))

imc = peso_user / (math.pow(altura_user,2))
print("Seu imc é: %.2f" % imc)
if imc < 20:
    print("Você está abaixo do peso. ")
elif imc >= 20 and imc < 25:
    print("Você está no peso normal. ")
elif imc >= 25 and imc < 30:
    print("Você está com sobre peso. ")
elif imc >= 30 and imc < 40:
    print("Você está obeso. ")
elif imc >= 40:
    print("Você está com obesidade mórbida. ")