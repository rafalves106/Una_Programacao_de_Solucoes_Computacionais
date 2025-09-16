"""
Implemente um algoritmo que retorne o valor da função abaixo após receber um valor qualquer de entrada:

f(x) =
{2x - 2, se x < 2}
{3, -2 <= x < 3}
{-x, 3 <= x}
"""

def calcular_funcao(x):
    if x < -2:
        return 2 * x + 2
    elif -2 <= x < 3:
        return 3
    else:
        return -x
    
input_value = float(input("Digite um número: "))
resultado = calcular_funcao(input_value)
print("O valor da função de x é: %.2f" % resultado)