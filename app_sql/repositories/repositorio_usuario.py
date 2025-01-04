from sqlite3 import IntegrityError
from models.usuarios import Usuario
from repositories.conexao import ConexaoDB

class RepositorioUsuario(ConexaoDB):
    
    NOME_TABELA = "usuarios"   

    def __init__(self):
        self.criar_tabela()

    def criar_tabela(self):
        sql = f"""CREATE TABLE IF NOT EXISTS {self.NOME_TABELA} (
                    id_usuario INTEGER PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    salt TEXT
        )"""
        
        self.executar_sql(sql, sql_tipo="CREATE_TABLE")        
    
        
    def cadastrar_usuario(self, usuario: Usuario):            
        
        sql = f"""INSERT INTO {self.NOME_TABELA} (username, senha, salt) VALUES (?,?,?)"""
        
        ultimo_id = self.executar_sql(sql, sql_tipo="INSERT", args=usuario.pegar_info_usuario())

        return ultimo_id[0]        

    
    def selecionar_todos_usuario(self):

        sql = f"""SELECT id_usuario, username FROM {self.NOME_TABELA} ORDER BY id_usuario"""

        resultado = self.executar_sql(sql, sql_tipo="SELECT")

        return resultado


    def selecionar_usuario_por_username(self, username):

        sql = f"""SELECT * FROM {self.NOME_TABELA} WHERE username = ?"""
        
        resultado = self.executar_sql(sql, sql_tipo="SELECT", args=username)

        return resultado


    def deletar_usuario(self, usuario_id):

        sql = f"""DELETE FROM {self.NOME_TABELA} WHERE usuario_id = ?"""

        resultado = self.executar_sql(sql, sql_tipo="DELETE", args=usuario_id)

        return resultado
    

    def executar_sql(self, sql, sql_tipo, args=None):
        
        # conexão com bando de dados
        conexao = self.criar_conexao()
        cursor = conexao.cursor()

        if sql_tipo == "CREATE_TABLE":
            cursor.execute(sql)
            conexao.commit() 
            retorno = "Tabela criada com sucesso."

        elif sql_tipo == "SELECT" and args is None: # select all
            retorno = cursor.execute(sql).fetchall()

        elif sql_tipo == "SELECT" and args is not None: # select one
            retorno = cursor.execute(sql, (args,)).fetchone()

        elif sql_tipo == "INSERT":
            cursor.execute(sql, args)
            conexao.commit()     
            retorno = cursor.execute("SELECT last_insert_rowid()").fetchone()

        elif sql_tipo == "DELETE":
            cursor.execute(sql,args)
            conexao.commit()     
            retorno = "Deletado com sucesso."
        
        return retorno
    

if __name__ == "__main__":

    # Testes

    # try:
    #     u = Usuario("barry", "jillsandwich")
    #     ultimo_id = RepositorioUsuario().cadastrar_usuario(u)
    #     print(ultimo_id)
    # except IntegrityError:
    #     print("Username já existe")

    resultado = RepositorioUsuario().selecionar_todos_usuario()
    for r in resultado:
        print(r)

    a = RepositorioUsuario().selecionar_usuario_por_username("chris")
    print(a)

    #resultado = RepositorioUsuario().deletar_usuario()
    #print(resultado)