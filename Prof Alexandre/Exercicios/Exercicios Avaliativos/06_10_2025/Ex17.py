"""
5. Solicite ao usuário que informe inicialmente a capacidade de um elevador em
kg. Solicite em seguida que informe o peso de cada pessoa que irá entrar no
elevador. O programa irá terminar quando a capacidade estiver esgotada.
Imprima no final a quantidade de pessoas que entraram no elevador, bem como
o peso total de todas essas pessoas.
"""

capacidade_elevador = int(input("Qual peso máximo que o elevador suporta em kg: "))
peso_usuario = float(input("Insira o peso do usuário que está entrando no elevador: "))

contador_pessoas = 0
peso_total = 0

while peso_usuario + peso_total <= capacidade_elevador and peso_usuario < capacidade_elevador:
    peso_total += peso_usuario
    contador_pessoas += 1
    peso_usuario = float(input("Insira o peso do outro usuário que está entrando no elevador: "))

print("------------------")
print("Limite de peso atingido no elevador.")
print(contador_pessoas,"pessoas entraram no elevador. ")
print("O peso total das pessoas que entraram no elevador foi", peso_total)
print("FIM DO PROGRAMA!")