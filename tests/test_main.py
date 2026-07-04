from fastapi.testclient import TestClient

from app import APP

CLIENT = TestClient(APP)

def test_index():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == "Olá, DevOps!"

# Criar um teste unitário para validar se a tarefa foi criada com sucesso
# CLIENT.post(...) (substituir pela string para criação de tarefa)
# Verificar se o código de status é 201
# Verificar se o retorno, quando tarefa é criada, é igual a {"mensagem": "OK"} ou conforme definido na sua API
# Verificar se o retorno, quando a tarefa já existe, é igual a {"mensagem" : "TAREFA JÁ EXISTE"} ou conforme definido na sua API

def test_criar_tarefa():
    requisicao = CLIENT.post("/tarefas?id=0&titulo=tarefa&descricao=descricao-tarefa")

    assert requisicao.status_code == 201
    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.post("/tarefas?id=0&titulo=tarefa&descricao=descricao-tarefa")
    assert requisicao.status_code == 201
    assert requisicao.json() == {"mensagem": "TAREFA JÁ EXISTE"}
