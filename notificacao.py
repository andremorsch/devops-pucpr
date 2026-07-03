from fastapi import FastAPI
from pydantic import BaseModel

APP_NOTIFICACAO = FastAPI()


class Notificacao(BaseModel):
	titulo: str
	data_finalizacao: str


@APP_NOTIFICACAO.post("/notificar")
async def notificar(notificacao: Notificacao):
	print(f"Tarefa finalizada: {notificacao.titulo} - Data: {notificacao.data_finalizacao}")
	return {"status": "ok"}