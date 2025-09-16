"""
2. Faça um programa para resolver equações de segundo grau (ax2 + bx + c = 0)
DELTA = b2 - 4 * a * c
1. DELTA < 0 - não existe raiz real
2. DELTA = 0 - existe somente uma raiz real x = (-b)/(2 * a)
3. DELTA > 0 - existem duas raízes reals
x1 = (-b + √A) /(2 * a)
x2 = (-b - √A) /(2 * a)
"""

import math

a = int(input("Informe o coeficiente A: "))
b = int(input("Informe o coeficiente B: "))
c = int(input("Informe o coeficiente C: "))

def calcula_delta(a, b, c):
    return (b**2) - (4 * a * c)

def calcula_raiz_unica(b, a):
    x = (-b) / (2 * a)
    print(f"Existe somente uma raiz real. O valor de X é: {x:.2f}")

def calcula_raizes_multiplas(delta, a, b):
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Existem duas raízes reais.")
    print(f"O valor de X1 é: {x1:.2f}")
    print(f"O valor de X2 é: {x2:.2f}")

if a == 0:
    print("Isso não é uma equação de segundo grau (o coeficiente A é zero).")
else:
    delta = calcula_delta(a, b, c)
    print(f"O valor de Delta é: {delta:.2f}")

    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        calcula_raiz_unica(b, a)
    else:
        calcula_raizes_multiplas(delta, a, b)