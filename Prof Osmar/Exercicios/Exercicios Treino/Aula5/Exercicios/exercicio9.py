"""
Uma academia de musculação possui a seguinte tabela para cobrança da mensalidade de seus clientes:

Homens
até 15 anos: 60,00
16 a 18 anos: 75,00
19 a 30 anos: 90,00
31 a 40 anos: 85,00
Acima de 40 anos: 80,00

Mulheres:
até 18 anos: 60,00
19 a 25 anos: 90,00
26 a 40 anos: 85,00
Acima de 40 anos: 80,00

Faça um programa que leia a idade e sexo do cliente, e imprima o valor da mensalidade que o mesmo deve pagar.

"""

idade = float(input("Digite a sua idade ( Anos ): "))
sexo = input("Digite o seu sexo ( M / F ): ")

def verifica_sexo_masculino(x):
    if x.lower() == "m":
        return True
    elif x.lower() == "f":
        return False
    else:
        return print("Sexo inválido. ")

def resultado(x):
    if (x >= 8 and x <= 15) and (verifica_sexo_masculino(sexo) == True):
        return 60
    
    elif (x >= 16 and x <= 18) and (verifica_sexo_masculino(sexo) == True):
        return 75
    
    elif (x >= 19 and x <= 30) and (verifica_sexo_masculino(sexo) == True):
        return 90
    
    elif (x >= 31 and x <= 40) and (verifica_sexo_masculino(sexo) == True):
        return 85
    
    elif (x > 40) and (verifica_sexo_masculino(sexo) == True):
        return 80
    
    elif (x >= 8 and x <= 18) and (verifica_sexo_masculino(sexo) == False):
        return 60
    
    elif (x >= 19 and x <= 25) and (verifica_sexo_masculino(sexo) == False):
        return 90
    
    elif (x >= 26 and x <= 40) and (verifica_sexo_masculino(sexo) == False):
        return 85
    
    elif (x > 40) and (verifica_sexo_masculino(sexo) == False):
        return 80
    
    else:
        return False
    
if resultado(idade) != False:
    print("O valor da mensalidade é", resultado(idade))
else:
    print("Idade é inválida. ")