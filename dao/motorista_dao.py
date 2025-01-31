from models.motorista import Motorista

motoristas = []

class MotoristaDAO:
    @staticmethod
    def adicionar_motorista(motorista: Motorista):
        motoristas.append(motorista)
    
    @staticmethod
    def listar_motoristas():
        return motoristas
    
    @staticmethod
    def buscar_motorista_por_id(id: int):
        for motorista in motoristas:
            if motorista.id == id:
                return motorista
        return None
    
    @staticmethod
    def atualizar_motorista(motorista_atualizado: Motorista):
        for i, motorista in enumerate(motoristas):
            if motorista.id == motorista_atualizado.id:
                motoristas[i] = motorista_atualizado
                return True
        return False
    
    @staticmethod
    def remover_motorista(id: int):
        global motoristas
        motoristas = [motorista for motorista in motoristas if motorista.id != id]
        