somaIdades = 0
contadorPeso = 0

for i in range(7):
    idade = int(input("Informe a idade de uma pessoa: "))
    peso = float(input("Informe o peso de uma pessoa em kg: "))
    
    if peso > 90:
        contadorPeso += 1
        
    somaIdades += idade
    
mediaIdades = somaIdades / 7
    
print("Quantidade de pessoas com mais de 90kg é", contadorPeso)
print("A média de idades foi: %.0f" % mediaIdades, "anos.")