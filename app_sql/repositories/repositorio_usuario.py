from repositories.auxiliar_db import AuxiliarDB
from models.usuarios import Usuario

from sqlite3 import IntegrityError

class RepositorioUsuario(AuxiliarDB):
    
    __NOME_TABELA = "usuarios"   

    def __init__(self):
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
    
        
    def cadastrar_usuario(self, usuario: Usuario) -> None:            
        
        sql = f"""INSERT INTO {self.__NOME_TABELA} (username, senha, salt) VALUES (?,?,?)"""
        
        info_usuario = (usuario.username, usuario.senha, usuario.salt)
        try:
            self.executar_sql(sql, info_usuario, comitar=True)
            self.fechar_conexao()
            return True
        except IntegrityError:
            self.fechar_conexao()
            return False


    def selecionar_usuario_por_username(self, username: str) -> tuple:

        sql = f"""SELECT * FROM {self.__NOME_TABELA} WHERE username = ?"""
              
        resultado = self.executar_sql(sql, (username,)).fetchone()        
        self.fechar_conexao()

        return resultado
    
    
    def selecionar_todos_usuario(self) -> list:

        sql = f"""SELECT id_usuario, username FROM {self.__NOME_TABELA} ORDER BY id_usuario"""

        resultado = self.executar_sql(sql).fetchall()
        self.fechar_conexao()
        
        return resultado
    
    
    def deletar_usuario(self, usuairo_id: int) -> None:

        sql = f"""DELETE FROM {self.__NOME_TABELA} WHERE id_usuario = ?"""
        
        self.executar_sql(sql, (usuairo_id,), comitar=True)
        self.fechar_conexao() 

