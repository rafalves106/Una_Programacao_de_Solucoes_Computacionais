"""
10. Faça um programa que leia um número e que imprima na tela se o número é
primo ou não.
"""

num = int(input("Digite um número: "))

verificador = 0
for i in range(2, num, 1):
    if num % i == 0:
        verificador += 1
        
if verificador >= 1:
    print("O número não é primo!")
    
if verificador == 0:
    print("O número é primo!")