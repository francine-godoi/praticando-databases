from sqlalchemy import Column, ForeignKey, Integer, String
from utils.conexao_db import Base


class Tarefa(Base):

    __tablename__ = "tarefas"

    id_tarefa = Column("id_tarefa", Integer, primary_key=True)
    descricao = Column("descricao", String, nullable=False)
    importancia = Column("importancia", String, nullable=False)
    status = Column("status", String, nullable=False)
    criado_em = Column("criado_em", String, nullable=False)
    finalizado_em = Column("finalizado_em", String, nullable=True)
    id_usuario = Column("id_usuario", ForeignKey("usuarios.id_usuario"))

    def __init__(
        self,
        id_usuario: int,
        descricao: str,
        importancia: str,
        criado_em: str,
        id_tarefa: int = None,
    ):
        self.id_tarefa = id_tarefa
        self.descricao = descricao
        self.importancia = importancia
        self.status = "A"
        self.criado_em = criado_em
        self.finalizado_em = None
        self.id_usuario = id_usuario

    def pegar_info_tarefa(self) -> tuple:
        return (self.id_usuario, self.descricao, self.importancia)
