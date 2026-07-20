# DevOps PUC PR - API de Gerenciamento de Tarefas

Esta aplicação é uma API REST desenvolvida em Python com FastAPI para gerenciar tarefas de forma simples e eficiente. O projeto foi estruturado para demonstrar conceitos de desenvolvimento backend, organização de serviços e integração entre componentes em uma arquitetura de microsserviços.

## Descrição da aplicação

A aplicação permite:
- Criar novas tarefas com título e descrição;
- Listar todas as tarefas cadastradas;
- Consultar uma tarefa específica pelo seu identificador;
- Atualizar o status de uma tarefa, incluindo marcação como concluída;
- Emitir notificações quando uma tarefa é finalizada;
- Verificar a saúde da API através de um endpoint de status.

A estrutura do projeto é composta por:
- uma API principal para gerenciamento de tarefas;
- um serviço de notificações;
- um gateway com Nginx para direcionar as requisições.

## Funcionalidades principais

- CRUD de tarefas;
- Endpoint de health check;
- Integração com serviço de notificações;
- Suporte a execução local e via containers Docker.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:
- Python 3.10 ou superior;
- pip;
- Docker e Docker Compose (opcional, para execução em containers).

## Execução local

### 1. Clone o repositório

```bash
git clone https://github.com/andremorsch/devops-pucpr.git
cd devops-pucpr
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API principal

```bash
uvicorn app.main:APP --reload --port 8000
```

A aplicação ficará disponível em:
- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/tarefas

### 5. Execute o serviço de notificações

Em outro terminal, execute:

```bash
uvicorn app.notificacao:APP_NOTIFICACAO --reload --port 8002
```

## Execução com Docker Compose

Para subir a aplicação com os serviços em containers:

```bash
docker compose up --build
```

A aplicação pode ser acessada pelo gateway Nginx em:
- http://localhost/

## Endpoints principais

### Health check
- GET /health

### Listar tarefas
- GET /tarefas

### Buscar tarefa por ID
- GET /tarefas/{id}

### Criar tarefa
- POST /tarefas

### Atualizar tarefa
- PUT /tarefas/{id}

### Excluir tarefa
- DELETE /tarefas/{id}

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Requests
- Docker
- Docker Compose
- Nginx
- Pytest

## Testes

Para executar os testes da aplicação:

```bash
pytest -q
```

## Observação

Este projeto é uma base simples para estudo e prática de conceitos de DevOps, API REST e containerização, sendo indicado para quem está começando a trabalhar com desenvolvimento backend e infraestrutura.
