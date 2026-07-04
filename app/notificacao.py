from fastapi import FastAPI
from datetime import datetime

APP_NOTIFICACAO = FastAPI()

# Criar uma rota para receber tarefa finalizada
# APP_NOTIFICACAO.post("/notificar")
# Entrada:
#   - Recebe título da tarefa e data de finalização da tarefa
# Saída:
#   - print no terminal

NOTIFICACOES = []

@APP_NOTIFICACAO.get("/notificar")
def listar_notificacoes():
    return NOTIFICACOES

@APP_NOTIFICACAO.post("/notificar")
def notificar(titulo: str, data_finalizacao: datetime):
    global NOTIFICACOES
    
    resultado = f"Tarefa '{titulo}' finalizada em {data_finalizacao}"
    print(resultado)

    NOTIFICACOES.append(resultado)

    return {"status": "OK"}