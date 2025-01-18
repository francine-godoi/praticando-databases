from models.base import Base
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Usuario(Base):

    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    salt: Mapped[str] = mapped_column(nullable=False)

    tarefas: Mapped[List["Tarefa"]] = relationship(back_populates='usuario')

    def __init__(
        self, username: str, senha: str, salt: str, id_usuario: int = None
    ) -> None:
        self.username = username
        self.senha = senha
        self.salt = salt
        self.id_usuario = id_usuario

    def __repr__(self) -> str:
        return f"Orm = Username: {self.username}, Senha: {self.senha}, Salt: {self.salt}"
