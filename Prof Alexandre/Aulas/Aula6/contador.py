counter = 0
adding = 0

for i in range(10):
    num = int(input("Digite um número:"))
    adding = adding + num
    
    if num < 0:
        counter += 1
        
print("Quantidade de números negativos:", counter)
print("Soma dos números:", adding)