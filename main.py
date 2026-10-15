
from fastapi import FastAPI

app = FastAPI(
    title="Projeto FastAPI",
    description="Projeto de curso complementar",
    version="1.0.0",
)


@app.get("/")
def inicio():
    return {
        "mensagem": "Minha API está funcionando!",
        "status": "online",
    }
