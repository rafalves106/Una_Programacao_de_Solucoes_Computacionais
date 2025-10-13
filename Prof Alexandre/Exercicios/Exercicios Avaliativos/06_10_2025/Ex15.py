"""
3. Faça um programa que solicite ao usuário que informe a matrícula e as três
notas de um conjunto de alunos. O programa deverá exibir a mensagem
informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota
maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O
programa irá terminar quando o usuário informar uma matrícula negativa.
"""

matricula = int(input("Informa a matrícula do aluno: "))
media = 0

while matricula >= 0:
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))
    
    media = nota_1 + nota_2 + nota_3
    
    if media >= 70:
        print("Aluno Aprovado!")
    elif media >= 60 and media < 70:
        print("Aluno fará exame!")
    elif media < 60:
        print("Aluno reprovado!")
        
    matricula = int(input("Informa a matrícula do aluno: "))