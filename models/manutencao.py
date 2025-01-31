from pydantic import BaseModel
from datetime import date

class Manutencao (BaseModel):
    id: int
    veiculo_id: int
    data: date
    descricao: str
    custo: float