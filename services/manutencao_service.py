from dao.manutencao_dao import ManutencaoDAO
from models.manutencao import Manutencao

class ManutencaoService:
    @staticmethod
    def adicionar_manutencao(manutencao: Manutencao):
        if ManutencaoDAO.buscar_manutencao_por_id(manutencao.id):
            raise ValueError("Manutenção com ID já existente.")
        ManutencaoDAO.adicionar_manutencao(manutencao)
    
    @staticmethod
    def listar_manutencoes():
        return ManutencaoDAO.listar_manutencoes()
    
    @staticmethod
    def buscar_manutencao_por_id(id: int):
        return ManutencaoDAO.buscar_manutencao_por_id(id)
    
    @staticmethod
    def atualizar_manutencao(manutencao: Manutencao):
        if not ManutencaoDAO.buscar_manutencao_por_id(manutencao.id):
            raise ValueError("Manutenção não encontrada.")
        ManutencaoDAO.atualizar_manutencao(manutencao)
    
    @staticmethod
    def remover_manutencao(id: int):
        if not ManutencaoDAO.buscar_manutencao_por_id(id):
            raise ValueError("Manutenção não encontrada.")
        ManutencaoDAO.remover_manutencao(id)
        