"""
Faça um programa para calcular a diferença em minutos entre dois horários informados como entrada. O usuário deverá informar a hora e minuto inicial e também a hora e minuto final.
"""

hora1 = int(input("Digite a hora inicial somente: "))
minutos1 = int(input("Digite o minuto final somente: "))

hora2 = int(input("Digite a hora final somente: "))
minutos2 = int(input("Digite o minuto final somente: "))

minutosDeHora1 = hora1 * 60
minutosDeHora2 = hora2 * 60
    
horaTotal1 = minutosDeHora1 + minutos1
horaTotal2 = minutosDeHora2 + minutos2

if horaTotal1 < horaTotal2:
    print("Diferença de", horaTotal2 - horaTotal1, "minutos")
elif horaTotal1 == horaTotal2:
    print("Os horários são os mesmos. Sem diferença.")
else:
    print("Diferença de", horaTotal1 - horaTotal2, "minutos")