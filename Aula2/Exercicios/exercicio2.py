"""
Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
- A idade da pessoa no ano atual
- A idade que a pessoa terá em 2050
"""

anoNasc = int(input("Digite o ano de seu nascimento: "));
anoAtual = 2025;
idadeAtual = anoAtual - anoNasc;

anoFuturo = 2050;
idadeFutura = anoFuturo - anoNasc;

print("A idade atual é:", idadeAtual, "anos.", "No ano de", anoFuturo, "ele terá:", idadeFutura, "anos.")