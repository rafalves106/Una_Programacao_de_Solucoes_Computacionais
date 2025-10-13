"""
1. Solicite ao usuário que informe um ano para validação. O ano válido deverá
estar entre 1900 e 2025. O programa irá terminar somente quando o ano
informado for válido.
"""

ano = int(input("Digite um ano (Ex: 1500):"))

while ano < 1900 or ano > 2025:
    ano = int(input("Digite um ano (Ex: 1500):"))
    
print("Fim do programa!")