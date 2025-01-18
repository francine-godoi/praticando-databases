import sqlite3
from config import BANCO_DADOS

class ConexaoDB():

    @classmethod
    def criar_conexao(cls):
        with sqlite3.connect(BANCO_DADOS) as conexao:
            return conexao
        
    