from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import BANCO_DADOS

class ConexaoDb:

    db = create_engine(f"sqlite:///{BANCO_DADOS}")

    def criar_session(self):
        with Session(self.db) as session:
            return session


