from repositories.conexao_db import ConexaoDB

class AuxiliarDB():
    
    def executar_sql(self, sql: str, args:tuple=(), comitar=False):               
        # conexão com bando de dados
        self.conexao = ConexaoDB.criar_conexao()
        self.cursor = self.conexao.cursor()

        self.cursor.execute(sql, args)
        
        if comitar:
            self.conexao.commit()

        return self.cursor     


    def fechar_conexao(self) -> None:
        self.cursor.close()
        self.conexao.close()