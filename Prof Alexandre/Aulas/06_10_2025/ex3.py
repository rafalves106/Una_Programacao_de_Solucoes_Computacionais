"""
3) Faça um programa que receba a nota final e o total de faltas de um conjunto indeterminado de alunos. Imprima:

a) A quantidade de alunos que obtiveram nota final maior ou igual a 90
b) A quantidade de alunos que foram reprovados por nota (nota menor que 70) ou por falta (quantidade de faltas maior ou igual a 20).
c) A maior e a menor nota
d) A média de notas da turma

O programa irá terminar quando o usuário informar uma nota negativa.
"""

notaFinal = float(input("Digite a nota final do aluno: "))


contadorAprovados = 0
contadorReprovados = 0
menorNota = 100
maiorNota = 0
quantidadeNotas = 0
somaNotas = 0

while notaFinal >= 0:    
    quantidadeNotas += 1
    somaNotas += notaFinal
    
    if notaFinal <= menorNota:
        menorNota = notaFinal
        
    if notaFinal >= maiorNota:
        maiorNota = notaFinal
    
    if notaFinal >= 90:
        contadorAprovados += 1
    elif notaFinal < 70 or quantidadeFaltas >= 20:
        contadorReprovados += 1
        
    quantidadeFaltas = int(input("Digite a quantidade de faltas do aluno: "))
    notaFinal = float(input("Digite a nota final do aluno: "))
    

if quantidadeNotas > 0:
    print("Quantidade de Alunos com nota maior ou igual a 90:", contadorAprovados)
    print("Quantidade de Alunos com nota menor que 70 ou com mais de 20 faltas:", contadorReprovados)
    print("A maior nota adicionada foi:", maiorNota)
    print("A menor nota adicionada foi:", menorNota)
    print("A média de notas da turma foi:", somaNotas / quantidadeNotas)
else:
    print("Fim do Programa, não foi adicionada nenhuma nota!")