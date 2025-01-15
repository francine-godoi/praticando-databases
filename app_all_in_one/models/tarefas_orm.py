from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from models.base import Base


class Tarefa(Base):

    __tablename__ = "tarefas"
    
    id_tarefa: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(nullable=False)
    importancia: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    criado_em: Mapped[str] = mapped_column(nullable=False)
    finalizado_em : Mapped[str] = mapped_column(nullable=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"))

    usuario: Mapped["Usuario"] = relationship(back_populates="tarefas")

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

    def __repr__(self) -> str:
        return f"Id tarefa: {self.id_tarefa}, Descrição: {self.descricao}, Importância: {self.importancia}"
