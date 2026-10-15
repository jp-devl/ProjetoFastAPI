
from fastapi import FastAPI
from routers.auth_routes import auth_router
from routers.order_routes import order_router

app = FastAPI(
    title="Projeto FastAPI",
    description="Projeto de curso complementar",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(order_router)


@app.get("/")
def inicio():
    return {
        "mensagem": "Minha API está funcionando!",
        "status": "online",
    }
