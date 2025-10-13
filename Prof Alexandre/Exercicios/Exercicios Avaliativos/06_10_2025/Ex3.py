"""
3. Leia um número e imprima a tabuada de multiplicar deste número. Por
exemplo, para o número 5:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
"""

num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(num, "X", i, "=", num * i)