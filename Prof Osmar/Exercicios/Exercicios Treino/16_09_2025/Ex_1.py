"""
1) Implemente um programa que receba as notas de provas de um aluno (A1 - 30 pontos e A2 - 30 pontos), bem como suas faltas. O programa deve avaliar se o aluno foi aprovado (nota maior ou igual a 70 e faltas menor que 25), reprovado (faltas maior ou igual a 25 ou nota menor que 45). Ainda, poderá fazer uma prova especial, valendo 30 pontos, se tiver pontuação maior ou igual a 40 e faltas menor que 25. Em caso de Prova Especial, receber o valor da nota da prova, fazer a substituição dela em relação a menor nota (A1 ou A2) e reavaliar se o aluno foi aprovado ou reprovado.
"""

nota_a1 = float(input("Digite a nota da sua A1: "))
nota_a2 = float(input("Digite a nota da sua A2: "))
nota_a3 = float(input("Digite a nota da sua A3: "))
faltas = int(input("Digite a quantidade de vezes que fatou: "))

total_nota = nota_a1 + nota_a2 + nota_a3

if total_nota >= 70 and faltas < 25:
    print('Aluno Aprovado. ')
    
elif total_nota < 45 or faltas >= 25:
        print('Aluno Reprovado. ')
        
elif total_nota >= 40 and faltas < 25:
    print('Aluno deve fazer prova especial. ')
    nota_especial = float(input('Qual foi a nota da prova especial? '))
    
    if nota_a1 < nota_a2 or nota_a1 == nota_a2:
        nota_a1 = nota_especial
    else:
        nota_a2 = nota_especial
        
    total_nota = nota_a1 + nota_a2 + nota_a3
        
    if total_nota >= 70:
        print('Aluno Aprovado. ')
    else:
        print('Aluno Reprovado. ')