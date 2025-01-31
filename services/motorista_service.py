from dao.motorista_dao import MotoristaDAO
from models.motorista import Motorista

class MotoristaService:
    @staticmethod
    def adicionar_motorista(motorista: Motorista):
        if MotoristaDAO.buscar_motorista_por_id(motorista.id):
            raise ValueError("Motorista com ID já existente.")
        MotoristaDAO.adicionar_motorista(motorista)
    
    @staticmethod
    def listar_motoristas():
        return MotoristaDAO.listar_motoristas()
    
    @staticmethod
    def buscar_motorista_por_id(id: int):
        return MotoristaDAO.buscar_motorista_por_id(id)
    
    @staticmethod
    def atualizar_motorista(motorista: Motorista):
        if not MotoristaDAO.buscar_motorista_por_id(motorista.id):
            raise ValueError("Motorista não encontrado.")
        MotoristaDAO.atualizar_motorista(motorista)
    
    @staticmethod
    def remover_motorista(id: int):
        if not MotoristaDAO.buscar_motorista_por_id(id):
            raise ValueError("Motorista não encontrado.")
        MotoristaDAO.remover_motorista(id)