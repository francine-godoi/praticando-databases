from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class ConexaoDb:

    db = create_engine("sqlite:///db/praticando_databases.db")

    def criar_session(self):
        with Session(self.db) as session:
            return session


