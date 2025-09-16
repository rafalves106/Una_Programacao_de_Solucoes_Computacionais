passagem = [
    {"destino": "Porto Seguro - BA", "valor": 600.00 },
    {"destino": "Rio de Janeiro - RJ", "valor": 800.00 },
    {"destino": "São Paulo - SP", "valor": 800.00 }
]

valorTotal = 0

for x in passagem:
    valorTotal += x["valor"]
    
if valorTotal > 2000:
    print("ALERTA: O valor total das passagens ultrapassou R$ 2000,00!")
else:
    print("O valor total das passagens é: R$ %.2f" % valorTotal)