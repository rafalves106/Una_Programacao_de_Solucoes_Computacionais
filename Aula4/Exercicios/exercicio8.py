"""
Uma família deseja realizar uma viagem a uma determinada cidade, e necessita de um programa para calcular seus gastos com o combustível.

Faça um programa que leia os seguintes dados:
- distância do local de origem ao destino (em km)
- o consumo médio de gasolina (km/l) do veículo
- o preço do litro de gasolina
- o consumo médio de álcool (km/l) do veículo 
- o preço do litro de álcool

Imprima o custo da viagem, considerando o trajeto de ida e volta.

O programa deve imprimir o custo tanto com a gasolina quanto com o álcool, para que a família possa fazer uma análise de qual combustível deverá utilizar.
"""

distancia = float(input("Digite a distância do trajeto(em km): "))

consumo_gas = float(input("Qual a média do consumo do veiculo com gasolina(km/l): "))
preco_gas = float(input("Qual o preço do litro da gasolina(R$)? "))

consumo_etanol = float(input("Qual a média do consumo do veiculo com álcool(km/l): "))
preco_etanol = float(input("Qual o preço do litro do álcool(R$)? "))

gasto_com_gas = (distancia / consumo_gas) * preco_gas
gasto_com_etanol = (distancia / consumo_etanol) * preco_etanol

print("-----------------------------------")
print("Você irá gastar R$ %.2f" % (gasto_com_gas * 2), "fazendo o trajeto de ida e volta com gasolina.")
print("Você irá gastar R$ %.2f" % (gasto_com_etanol * 2), "fazendo o trajeto de ida e volta com álcool.")
print("Você irá gastar R$ %.2f" % (gasto_com_etanol + gasto_com_gas), "fazendo o trajeto deida e volta com metade álcool e metade gasolina.")
print("-----------------------------------")