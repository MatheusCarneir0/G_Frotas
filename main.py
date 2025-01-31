from fastapi import FastAPI
from controllers.veiculo_controller import router as veiculo_router
from controllers.motorista_controller import router as motorista_router
from controllers.manutencao_controller import router as manutencao_router

app = FastAPI()

app.include_router(veiculo_router, prefix="/api")
app.include_router(motorista_router, prefix="/api")
app.include_router(manutencao_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Bem-vindo ao sistema de gerenciamento de frota de veículos!"}