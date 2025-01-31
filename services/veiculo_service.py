from dao.veiculo_dao import VeiculoDAO
from models.veiculo import Veiculo

class VeiculoService:
    @staticmethod
    def adicionar_veiculo(veiculo: Veiculo):
        if VeiculoDAO.buscar_veiculo_por_id(veiculo.id):
            raise ValueError("Veículo com ID já existente.")
        VeiculoDAO.adicionar_veiculo(veiculo)
    
    @staticmethod
    def listar_veiculos():
        return VeiculoDAO.listar_veiculos()
    
    @staticmethod
    def buscar_veiculo_por_id(id: int):
        return VeiculoDAO.buscar_veiculo_por_id(id)
    
    @staticmethod
    def atualizar_veiculo(veiculo: Veiculo):
        if not VeiculoDAO.buscar_veiculo_por_id(veiculo.id):
            raise ValueError("Veículo não encontrado.")
        VeiculoDAO.atualizar_veiculo(veiculo)
    
    @staticmethod
    def remover_veiculo(id: int):
        if not VeiculoDAO.buscar_veiculo_por_id(id):
            raise ValueError("Veículo não encontrado.")
        VeiculoDAO.remover_veiculo(id)