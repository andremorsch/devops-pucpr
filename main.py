from fastapi import FastAPI, HTTPException
from datetime import datetime

LISTA_TAREFAS = []
APP = FastAPI()

def nova_tarefa(id: int, titulo: str, descricao: str):
    """Função auxiliar para criar uma tarefa usando dicionário (`dict`)"""
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }

@APP.get("/")
def index():
    return "Olá, DevOps!"

@APP.get("/tarefas")
def listar_tarefas():
    # Lista tarefas (somente id e titulo)
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS

    tarefas = []
    
    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": tarefa['titulo']}
        tarefas.append(info)

    return tarefas

@APP.get("/tarefas/{id}")
def listar_tarefa_especifica(id: int):
    mensagem_padrao = {"mensagem": "Não existe nenhuma tarefa"}
    if len(LISTA_TAREFAS) == 0:
        return mensagem_padrao
    
    # ID da tarefa é o índice na lista
    if id >= 0 and id < len(LISTA_TAREFAS):
        return LISTA_TAREFAS[id]
    
    return mensagem_padrao

@APP.post("/tarefas", status_code=201)
def criar_tarefa(titulo: str, descricao: str):
    nova_id = len(LISTA_TAREFAS)
    tarefa = nova_tarefa(nova_id, titulo, descricao)
    LISTA_TAREFAS.append(tarefa)
    return tarefa

@APP.put("/tarefas/{id}")
def atualizar_tarefa(id: int, titulo: str, descricao: str, concluido: bool):
    if id < 0 or id >= len(LISTA_TAREFAS):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa = LISTA_TAREFAS[id]
    tarefa["titulo"] = titulo
    tarefa["descricao"] = descricao
    tarefa["concluido"] = concluido
    return tarefa

@APP.delete("/tarefas/{id}", status_code=200)
def deletar_tarefa(id: int):
    if id < 0 or id >= len(LISTA_TAREFAS):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa_removida = LISTA_TAREFAS.pop(id)
    return {"mensagem": "Tarefa removida com sucesso", "tarefa": tarefa_removida}