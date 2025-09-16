"""
Uma loja de roupas vende os produtos em duas modalidades: à vista (com 10% de desconto) ou a prazo (em até 5 parcelas). Faça um programa que receba o preço do produto e o número de parcelas, e informe o valor de cada prestação, bem como o valor à vista, para que o cliente possa analisar a melhor forma de pagamento.
"""

resposta = str(input("Deseja saber o valor a vista e a prazo de um produto? (Sim/Não) "))
escolha = (resposta.lower() == "sim")

while escolha:
    
    valor_produto = float(input("Digite o valor do produto: "))
    while valor_produto <= 0:
        valor_produto = float(input("Digite um valor positivo: "))
    
    n_parcelas = int(input("Digite o número de parcelas (Máx 5): "))
    while n_parcelas <= 0 or n_parcelas > 5:
        n_parcelas = int(input("Digite um valor permitido (Máx 5): "))
        
    a_vista = valor_produto * 0.9
    a_prazo = valor_produto / n_parcelas
    
    print("---------------------------------------")
    print("O valor do produto a vista é R$ %.2f" % a_vista, "!")
    print("O valor do produto dividido em", n_parcelas, "parcelas é R$ %.2f" % a_prazo, "por parcela!")
    print("---------------------------------------")
    
    resposta = str(input("Deseja saber de outro produto? (Sim/Não) "))
    escolha = (resposta.lower() == "sim")
    
print("Obrigado por utilizar o serviço.")
    