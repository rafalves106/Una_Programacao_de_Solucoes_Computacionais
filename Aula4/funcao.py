def calcula_troco(valor_total, valor_pago):
    troco = valor_pago - valor_total
    return troco

valor_total = float(input("Qual o valor total da sua compra? (R$) "))
valor_pago = float(input("Quanto você deu para pagar a sua compra? (R$) "))

if valor_pago < valor_total:
    print("O valor pago é inferior ao valor total. ")
else:
    print("O seu troco é de: R$%.2f" % calcula_troco(valor_total, valor_pago))