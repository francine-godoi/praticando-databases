from sqlite3 import IntegrityError

from models.usuarios import Usuario
from repositories.auxiliar_db import AuxiliarDB


class RepositorioUsuario(AuxiliarDB):

    __NOME_TABELA = "usuarios"

    def __init__(self) -> None:
        self.conexao = None
        self.cursor = None
        self.criar_tabela_usuario()

    def criar_tabela_usuario(self) -> None:
        sql = f"""CREATE TABLE IF NOT EXISTS {self.__NOME_TABELA} (
                    id_usuario INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    salt TEXT NOT NULL
        )"""

        self.executar_sql(sql)
        self.fechar_conexao()

    def cadastrar_usuario(self, usuario: Usuario) -> int:

        # trunk-ignore(bandit/B608)
        sql = f"""INSERT INTO {self.__NOME_TABELA} (username, senha, salt) VALUES (?,?,?)"""

        info_usuario = (usuario.username, usuario.senha, usuario.salt)
        try:
            resultado = self.executar_sql(sql, info_usuario, comitar=True).rowcount
            self.fechar_conexao()
            return resultado
        except IntegrityError:
            self.fechar_conexao()
            return 0

    def selecionar_usuario_por_username(self, username: str) -> Usuario:

        # trunk-ignore(bandit/B608)
        sql = f"""SELECT * FROM {self.__NOME_TABELA} WHERE username = ?"""

        resultado = self.executar_sql(sql, (username,)).fetchone()
        self.fechar_conexao()

        # 1 = username, 2 = senha, 3 = salt, 1 = id_usuario
        usuario = Usuario(resultado[1], resultado[2], resultado[3], resultado[0])

        return usuario
