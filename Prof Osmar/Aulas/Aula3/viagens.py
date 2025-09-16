listaDeViagens = [
    {"nome": "Viagem para São Paulo", "status": "No prazo"},
    {"nome": "Viagem para o Rio de Janeiro", "status": "Atrasada"},
    {"nome": "Viagem para Curitiba", "status": "Concluída"},
    {"nome": "Viagem para Belo Horizonte", "status": "Atrasada"}
]

for x in listaDeViagens:
    if x["status"] == 'Atrasada':
        print("Alerta!!! A", x["nome"], "está atrasada!!!")