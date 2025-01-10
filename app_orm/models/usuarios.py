from sqlalchemy import Column, String, Integer
from utils.conexao_db import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id_usuario = Column("id_usuario", Integer, primary_key=True)
    username = Column("username", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    salt = Column("salt", String, nullable=False)

    def __init__(self, username: str, senha: str, salt: str):
        self.username = username        
        self.senha = senha   
        self.salt = salt

    def pegar_info_usuario(self) -> tuple:
        return (self.username, self.senha, self.salt)