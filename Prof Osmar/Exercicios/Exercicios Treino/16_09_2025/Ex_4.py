"""
4) Faça um programa que receba:

(a) O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, isto é, um número entre 1 e 10.

(b) O peso do produto em quilos.

(c) O código do país de origem, supondo que a digitação do código seja sempre válida, isto é, um número inteiro entre 1 e 3.

(d) Sabendo que:
- Para País de origem “1” o imposto é de 0%;
- Para País de origem “2” o imposto é de 15%;
- Para País de origem “3” o imposto é de 25%;

- Para o código do produto “1 a 4 ” o preço por grama é $10;
- Para o código do produto “5 a 7 ” o preço por grama é $25;
- Para o código do produto “8 a 10 ”o preço por grama é $35.

(e) Calcule e mostre:
• O peso do produto convertido em gramas;
• O preço total do produto comprado;
• O valor do imposto, sabendo que ele é cobrado sobre o preço total do produto comprado e depende do país de origem;
• O preço total do produto mais imposto.
"""

cod_produto = int(input("Digite o código do produto (1 a 10): "))
kilos_produto = float(input("Digite o peso do produto em quilo: "))
cod_pais = int(input("Digite o código do país de origem do produto (1 a 3): "))

peso_em_gramas = kilos_produto * 1000

preco_por_grama = 0
if (cod_produto >= 1 and cod_produto <= 4):
    preco_por_grama = 10
elif (cod_produto >= 5 and cod_produto <= 7):
    preco_por_grama =  25
elif (cod_produto >= 8 and cod_produto <= 10):
    preco_por_grama = 35

preco_total_por_grama = preco_por_grama * peso_em_gramas

valor_imposto = 0
if (cod_pais == 1):
    valor_imposto = 0
elif (cod_pais == 2):
    valor_imposto = preco_total_por_grama * 0.25
elif (cod_pais == 3):
    valor_imposto = preco_total_por_grama * 0.35
        
print("O peso do produto convertido em gramas é:", peso_em_gramas)
print("O preço total do produto calculado pelas gramas é:", preco_por_grama)
print("O valor que deverá ser pago em impostos pelo produto é:", preco_total_por_grama)
print("O valor total do produto com impostos é:", preco_total_por_grama + valor_imposto)