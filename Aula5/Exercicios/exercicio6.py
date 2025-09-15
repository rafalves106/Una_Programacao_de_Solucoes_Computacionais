"""
Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados.
"""

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

if x < (y + z) and y < (x + z) and z < (x + y):
    print("Os valores formam um triângulo. ")
else:
    print("Os valores não formam um triângulo. ")