class Tarefa:
    
    def __init__(self, id_usuario: int, descricao: str, importancia: str, id_tarefa: int = None):
        self.id_usuario = id_usuario
        self.descricao = descricao
        self.importancia = importancia
        self.id_tarefa = id_tarefa

    def pegar_info_tarefa(self) -> tuple:
        return (self.id_usuario, self.descricao, self.importancia)