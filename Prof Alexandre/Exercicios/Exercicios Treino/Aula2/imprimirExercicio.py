j = 1;
limite = int(input("Digite um limite para o contador(máx 100): "))

while limite > 100:
    limite = int(input("Digite um limite para o contador(máx 100): "))

if limite <= 100:
    while j <= limite:
        print(j)
        j+=1