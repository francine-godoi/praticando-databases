from pymongo import MongoClient

class ConexaoDb:

    def __init__(self):
        self.criar_conexao()

    @classmethod
    def criar_conexao(cls):
        connection_string = "mongodb://localhost:27017/"
        client = MongoClient(connection_string)
        return client

    @classmethod
    def pegar_db(cls):
        client = cls.criar_conexao()
        db = client.praticando_nosql_database
        return db