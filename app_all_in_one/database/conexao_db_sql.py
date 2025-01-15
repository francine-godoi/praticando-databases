import sqlite3

class ConexaoDB:

    BANCO_DADOS = "db/praticando_databases.db"

    @classmethod
    def criar_conexao(cls):
        with sqlite3.connect(cls.BANCO_DADOS) as conexao:
            return conexao
        
    