from pydantic import BaseModel

class Veiculo(BaseModel):
    id: int
    marca: str
    ano: int
    placa: str
    status: str # |Dispinível| |Em Manutenção| |Em Uso|
