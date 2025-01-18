from pymongo import MongoClient
from config import CONNECTION_STRING

class ConexaoDb:

    def __init__(self):
        self.criar_conexao()

    @classmethod
    def criar_conexao(cls):
        client = MongoClient(CONNECTION_STRING)
        return client

    @classmethod
    def pegar_db(cls):
        client = cls.criar_conexao()
        db = client.praticando_nosql_database
        return db