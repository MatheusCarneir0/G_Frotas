from models.manutencao import Manutencao

manutencoes = []

class ManutencaoDAO:
    @staticmethod
    def adicionar_manutencao(manutencao: Manutencao):
        manutencoes.append(manutencao)
    
    @staticmethod
    def listar_manutencoes():
        return manutencoes
    
    @staticmethod
    def buscar_manutencao_por_id(id: int):
        for manutencao in manutencoes:
            if manutencao.id == id:
                return manutencao
        return None
    
    @staticmethod
    def atualizar_manutencao(manutencao_atualizada: Manutencao):
        for i, manutencao in enumerate(manutencoes):
            if manutencao.id == manutencao_atualizada.id:
                manutencoes[i] = manutencao_atualizada
                return True
        return False
    
    @staticmethod
    def remover_manutencao(id: int):
        global manutencoes
        manutencoes = [manutencao for manutencao in manutencoes if manutencao.id != id]