"""
Faça um programa para simular a compra de produtos em um supermercado. O usuário irá informar o nome e o preço de três produtos comprados pelo cliente e, em seguida, o valor que o cliente forneceu para pagar a compra. O programa deverá imprimir o valor total da compra e o valor do troco a ser retornado ao cliente.

A saída do programa deverá ser a seguinte:
---------- 	--------------
Produto	Valor
---------- 	--------------
Prod1		valor1
Prod2		valor2
Prod3		valor3
----------------------------------------
Total da Compra: R$ total
----------------------------------------
Valor Pago: R$ valor Pago
Troco: R$ troco
----------------------------------------
"""

produtos = [{"nome" : "", "valor" : 0} for _ in range(3)]
total_compra = 0

for _ in produtos:
    _["nome"] = str(input("Digite o nome do produto: "))
    _["valor"] = int(input("Digite o valor do produto (R$): "))
    
valor_pago = float(input("Qual foi o valor fornecido para a compra? (R$) "))

print("---------- 	--------------")
print("Produto	Valor")
print("---------- 	--------------")
    
for prod in produtos:
    print(prod["nome"], "%.2f" % prod["valor"])
    total_compra += float(prod["valor"])

troco = valor_pago - total_compra
    
print("----------------------------------------")
print("Total da Compra: R$ %.2f" % total_compra)
print("----------------------------------------")
print("Valor Pago: R$ %.2f" % valor_pago)
print("Troco: R$ %.2f" % troco)
print("----------------------------------------")