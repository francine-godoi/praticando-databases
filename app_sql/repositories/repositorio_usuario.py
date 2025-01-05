from models.usuarios import Usuario
from repositories.conexao_db import ConexaoDB

class RepositorioUsuario():
    
    NOME_TABELA = "usuarios"   

    def __init__(self):
        self.conexao = None
        self.cursor = None
        self.criar_tabela_usuario()


    def criar_tabela_usuario(self) -> None:
        sql = f"""CREATE TABLE IF NOT EXISTS {self.NOME_TABELA} (
                    id_usuario INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    salt TEXT
        )"""
        
        self.executar_sql(sql)  
        self.fechar_conexao()
    
        
    def cadastrar_usuario(self, usuario: Usuario) -> None:            
        
        sql = f"""INSERT INTO {self.NOME_TABELA} (username, senha, salt) VALUES (?,?,?)"""
        
        info_usuario = usuario.pegar_info_usuario()
        self.executar_sql(sql, info_usuario, comitar=True)
        self.fechar_conexao()


    def deletar_usuario(self, usuairo_id: int) -> None:

        sql = f"""DELETE FROM {self.NOME_TABELA} WHERE id_usuario = ?"""
        
        self.executar_sql(sql, (usuairo_id,), comitar=True)
        self.fechar_conexao() 

    
    def selecionar_todos_usuario(self) -> list:

        sql = f"""SELECT id_usuario, username FROM {self.NOME_TABELA} ORDER BY id_usuario"""

        resultado = self.executar_sql(sql).fetchall()
        self.fechar_conexao()
        
        return resultado


    def selecionar_usuario_por_username(self, username: str) -> tuple:

        sql = f"""SELECT * FROM {self.NOME_TABELA} WHERE username = ?"""
              
        resultado = self.executar_sql(sql, (username,)).fetchone()        
        self.fechar_conexao()

        return resultado

   
    def executar_sql(self, sql, args:tuple=None, comitar=False):
               
        # conexão com bando de dados
        self.conexao = ConexaoDB.criar_conexao()
        self.cursor = self.conexao.cursor()

        if args:
            self.cursor.execute(sql, args)
        else:
            self.cursor.execute(sql)

        if comitar:
            self.conexao.commit()

        return self.cursor     


    def fechar_conexao(self) -> None:
        self.cursor.close()
        self.conexao.close()