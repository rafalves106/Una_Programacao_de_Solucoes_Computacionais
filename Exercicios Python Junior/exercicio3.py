"""
3.  Crie uma função que inverta uma string sem usar métodos de biblioteca.
"""

def inverter(texto):
    valor_invertido = ""
    
    for i in range(len(texto) -1, -1, -1):
        valor_invertido += texto[i]
        
    return valor_invertido

valor = "Teste de Inversão de String"
inverter(valor)

print("Texto normal:", valor)
print("Texto invertido:", inverter(valor))