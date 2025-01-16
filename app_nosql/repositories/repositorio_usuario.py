from repositories.conexao_db import ConexaoDb
from models.usuarios import Usuario


class RepositorioUsuario():

    def __init__(self) -> None:
        self.db = ConexaoDb.pegar_db()
        self.collection_usuario = self.criar_tabela_usuario()

    def criar_tabela_usuario(self) -> None:
        collection_usuario = self.db.usuarios
        return collection_usuario

    def cadastrar_usuario(self, usuario: Usuario) -> int:
        #TODO username tem que ser unico
        info_usuario = {'username': usuario.username,
                        'senha': usuario.senha,
                        'salt': usuario.salt}        
        
        id_cadastrado = self.collection_usuario.insert_one(info_usuario).inserted_id
        return id_cadastrado

    def selecionar_usuario_por_username(self, username: str) -> Usuario | int:
        pass
        # sql = f"""SELECT * FROM {self.__NOME_TABELA} WHERE username = ?"""

        # resultado = self.executar_sql(sql, (username,)).fetchone()
        # self.fechar_conexao()

        # if not resultado:
        #     return 0
        # # 1 = username, 2 = senha, 3 = salt, 1 = id_usuario
        # usuario = Usuario(resultado[1], resultado[2], resultado[3], resultado[0])

        # return usuario
