from fastapi import APIRouter, HTTPException
from models.veiculo import Veiculo
from services.veiculo_service import VeiculoService

router = APIRouter()

@router.post("/veiculos/")
def adicionar_veiculo(veiculo: Veiculo):
    try:
        VeiculoService.adicionar_veiculo(veiculo)
        return {"message": "Veículo adicionado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/veiculos/")
def listar_veiculos():
    return VeiculoService.listar_veiculos()

@router.get("/veiculos/{id}")
def buscar_veiculo(id: int):
    veiculo = VeiculoService.buscar_veiculo_por_id(id)
    if veiculo:
        return veiculo
    raise HTTPException(status_code=404, detail="Veículo não encontrado")

@router.put("/veiculos/{id}")
def atualizar_veiculo(id: int, veiculo: Veiculo):
    if id != veiculo.id:
        raise HTTPException(status_code=400, detail="ID do veículo não corresponde")
    try:
        VeiculoService.atualizar_veiculo(veiculo)
        return {"message": "Veículo atualizado com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/veiculos/{id}")
def remover_veiculo(id: int):
    try:
        VeiculoService.remover_veiculo(id)
        return {"message": "Veículo removido com sucesso!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))