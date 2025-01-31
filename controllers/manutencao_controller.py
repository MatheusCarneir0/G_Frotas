from fastapi import APIRouter, HTTPException
from models.manutencao import Manutencao
from services.manutencao_service import ManutencaoService

router = APIRouter()

@router.post("/manutencoes/")
def adicionar_manutencao(manutencao: Manutencao):
    try:
        ManutencaoService.adicionar_manutencao(manutencao)
        return {"message": "Manutenção adicionada com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/manutencoes/")
def listar_manutencoes():
    return ManutencaoService.listar_manutencoes()

@router.get("/manutencoes/{id}")
def buscar_manutencao(id: int):
    manutencao = ManutencaoService.buscar_manutencao_por_id(id)
    if manutencao:
        return manutencao
    raise HTTPException(status_code=404, detail="Manutenção não encontrada")

@router.put("/manutencoes/{id}")
def atualizar_manutencao(id: int, manutencao: Manutencao):
    if id != manutencao.id:
        raise HTTPException(status_code=400, detail="ID da manutenção não corresponde")
    try:
        ManutencaoService.atualizar_manutencao(manutencao)
        return {"message": "Manutenção atualizada com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/manutencoes/{id}")
def remover_manutencao(id: int):
    try:
        ManutencaoService.remover_manutencao(id)
        return {"message": "Manutenção removida com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))