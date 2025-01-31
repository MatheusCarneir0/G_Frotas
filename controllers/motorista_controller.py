from fastapi import APIRouter, HTTPException
from models.motorista import Motorista
from services.motorista_service import MotoristaService

router = APIRouter()

@router.post("/motoristas/")
def adicionar_motorista(motorista: Motorista):
    try:
        MotoristaService.adicionar_motorista(motorista)
        return {"message": "Motorista adicionado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/motoristas/")
def listar_motoristas():
    return MotoristaService.listar_motoristas()

@router.get("/motoristas/{id}")
def buscar_motorista(id: int):
    motorista = MotoristaService.buscar_motorista_por_id(id)
    if motorista:
        return motorista
    raise HTTPException(status_code=404, detail="Motorista não encontrado")

@router.put("/motoristas/{id}")
def atualizar_motorista(id: int, motorista: Motorista):
    if id != motorista.id:
        raise HTTPException(status_code=400, detail="ID do motorista não corresponde")
    try:
        MotoristaService.atualizar_motorista(motorista)
        return {"message": "Motorista atualizado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/motoristas/{id}")
def remover_motorista(id: int):
    try:
        MotoristaService.remover_motorista(id)
        return {"message": "Motorista removido com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))