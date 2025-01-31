from models.veiculo import Veiculo

veiculos = []

class VeiculoDAO:
    @staticmethod
    def adicionar_veiculo(veiculo: Veiculo):
        veiculos.append(veiculo)
    
    @staticmethod
    def listar_veiculos():
        return veiculos
    
    @staticmethod
    def buscar_veiculo_por_id(id: int):
        for veiculo in veiculos:
            if veiculo.id == id:
                return veiculo
        return None
    
    @staticmethod
    def atualizar_veiculo(veiculo_atualizado: Veiculo):
        for i, veiculo in enumerate(veiculos):
            if veiculo.id == veiculo_atualizado.id:
                veiculos[i] = veiculo_atualizado
                return True
        return False
    
    @staticmethod
    def remover_veiculo(id: int):
        global veiculos
        veiculos = [veiculo for veiculo in veiculos if veiculo.id != id]
        