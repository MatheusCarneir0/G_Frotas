from pydantic import BaseModel

class Motorista(BaseModel):
    id: int
    nome: str
    cnh: str
    status: str # |Disponível| |Em Viagem|
    