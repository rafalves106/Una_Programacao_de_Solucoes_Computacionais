for i in range(5):
    temp = float(input("Digite a temperatura: "))
    if i == 0:
        maior = temp
        menor = temp
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
    
print("Maior temperatura:", maior)
print("Menor temperatura:", menor)