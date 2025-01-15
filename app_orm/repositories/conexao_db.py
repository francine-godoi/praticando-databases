from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

class ConexaoDb:

    db = create_engine("sqlite:///db/praticando_databases.db")
    Base = declarative_base()

    def pegar_base(self):
        return self.Base

    def criar_session(self):
        with Session(self.db) as session:
            return session


