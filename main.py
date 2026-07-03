from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Optional
import requests

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
def atualizar_tarefa(id: int, titulo: Optional[str] = None, descricao: Optional[str] = None, concluido: Optional[bool] = None):
    if id < 0 or id >= len(LISTA_TAREFAS):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa = LISTA_TAREFAS[id]
    prev_concluido = tarefa.get("concluido", False)

    # Atualizar somente os campos fornecidos
    if titulo is not None:
        tarefa["titulo"] = titulo
    if descricao is not None:
        tarefa["descricao"] = descricao
    if concluido is not None:
        tarefa["concluido"] = concluido

    # Se a tarefa foi atualizada para concluída agora, chamar serviço de notificação
    if (not prev_concluido) and (concluido is True):
        try:
            payload = {
                "titulo": tarefa["titulo"],
                "data_finalizacao": datetime.now().isoformat()
            }
            requests.post("http://localhost:8001/notificar", json=payload, timeout=2)
        except Exception as e:
            print(f"Falha ao notificar: {e}")

    return tarefa

@APP.delete("/tarefas/{id}", status_code=200)
def deletar_tarefa(id: int):
    if id < 0 or id >= len(LISTA_TAREFAS):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    tarefa_removida = LISTA_TAREFAS.pop(id)
    return {"mensagem": "Tarefa removida com sucesso", "tarefa": tarefa_removida}