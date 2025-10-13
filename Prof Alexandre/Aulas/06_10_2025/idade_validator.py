idade = int(input("Digite a sua idade: "))

while idade < 0:
    idade = int(input("Idade inválida. Digite a sua idade novamente: "))
    
print("Idade válida:", idade)