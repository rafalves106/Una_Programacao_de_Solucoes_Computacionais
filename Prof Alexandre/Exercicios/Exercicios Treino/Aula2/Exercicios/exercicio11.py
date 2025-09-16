import math

"""
Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação (considere que os valores informados sempre retornarão raízes reais para a equação).
"""

a = float(input("Informe o coeficiente de 'A' (Não pode ser zero): "))

while a == 0:
    a = float(input("'A' não pode ser igual a 0. Digite novamente: "))
    
if a < 0 or a > 0:
        b = float(input("Informe o coeficiente de 'B': "))
        c = float(input("Informe o coeficiente de 'C': "))
        
        delta = math.pow(b,2) - 4 * a * c
        
        print(delta)
        if delta < 0: 
            print("Não existe raiz para essa equação.")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            
            print("As raízes da equação são %.2f" % x1, "e %.2f" % x2);