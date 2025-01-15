from datetime import datetime


class Tarefa:

    def __init__(
        self,
        id_usuario: int,
        descricao: str,
        importancia: str,
        id_tarefa: int = None,
        status: str = "A",
        criado_em: str = datetime.today().strftime("%d/%m/%Y"),
        finalizado_em: str = None,
    ) -> None:
        self.id_tarefa = id_tarefa
        self.descricao = descricao
        self.importancia = importancia
        self.status = status
        self.criado_em = criado_em
        self.finalizado_em = finalizado_em
        self.id_usuario = id_usuario

    def pegar_info_tarefa(self) -> tuple:
        return (self.id_usuario, self.descricao, self.importancia)
