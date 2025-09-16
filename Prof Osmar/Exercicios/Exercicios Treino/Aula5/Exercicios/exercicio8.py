"""
Um determinado hotel cobra R$ 500,00 a diária e mais uma taxa de serviços. Faça um programa que leia o número de diárias e calcule o total a ser pago pelo cliente, sabendo-se que a taxa de serviços é de: 
R$ 15,00 por dia, se número de diárias < 15 
R$ 10,00 por dia, se número de diárias = 15 
R$ 5,00 por dia, se número de diárias > 15 
"""

def verifica_valor(x):
    if x > 0:
        return True

def calcula_taxa(x):
        if x > 0 < 15:
            x = x * 15
        elif x == 15:
            x = x * 10
        else:
            x = x * 5
        return x
        
def calcular_diarias(x):
    if x > 0:         
        x = x * 500
        return x

diarias = int(input("Digite o número de diárias do cliente: "))

if verifica_valor(diarias) == True:
    print("O valor que deverá ser cobrado do cliente pelas diárias é de: R$", calcular_diarias(diarias))
    print("e o valor das taxas de serviço é de: R$", calcula_taxa(diarias))
else:
    print("Valor inválido. ")