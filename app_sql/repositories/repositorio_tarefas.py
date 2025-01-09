from sqlite3 import IntegrityError
from models.tarefas import Tarefa
from repositories.auxiliar_db import AuxiliarDB
from datetime import date

class RepositorioTarefa(AuxiliarDB):

    __NOME_TABELA = "tarefas"
    __FOREIGN_TABELA = "usuarios"

    def __init__(self):
        self.conexao = None
        self.cursor = None
        self.criar_tabela_tarefas()


    def criar_tabela_tarefas(self) -> None:

        sql = f"""CREATE TABLE IF NOT EXISTS {self.__NOME_TABELA} (
                    id_tarefa INTEGER PRIMARY KEY,
                    id_usuario INTEGER,
                    descricao TEXT NOT NULL,
                    importancia TEXT NOT NULL,
                    status TEXT NOT NULL,
                    criado_em TEXT NOT NULL,
                    finalizado_em TEXT,
                    FOREIGN KEY (id_usuario) REFERENCES {self.__FOREIGN_TABELA} (id_usuario)
        )"""

        self.executar_sql(sql)
        self.fechar_conexao()
    

    def cadastrar_tarefa(self, tarefa: Tarefa) -> int:

        sql = f"""INSERT INTO {self.__NOME_TABELA} (id_usuario, descricao, importancia, status, criado_em) VALUES(?,?,?,?,?)"""
        
        data = date.today().strftime("%d/%m/%Y")
        info_tarefa = (tarefa.id_usuario, tarefa.descricao, tarefa.importancia, "A", data)
        resultado = self.executar_sql(sql, info_tarefa, comitar=True).rowcount
        self.fechar_conexao()

        return resultado


    def editar_tarefa(self, tarefa:Tarefa) -> int:

        sql = f"""UPDATE {self.__NOME_TABELA} SET descricao = ?, importancia = ? WHERE id_tarefa = ? AND status = 'A'"""

        info_tarefa = (tarefa.descricao, tarefa.importancia, tarefa.id_tarefa)
        resultado = self.executar_sql(sql, info_tarefa, comitar=True).rowcount
        self.fechar_conexao()

        return resultado

    
    def deletar_tarefa(self, id_tarefa:int) -> int:

        sql = f"""DELETE FROM {self.__NOME_TABELA} WHERE id_tarefa = ? AND status = 'A'"""

        resultado = self.executar_sql(sql, (id_tarefa,), comitar=True).rowcount
        self.fechar_conexao()

        return resultado

        
    def finalizar_tarefa(self, id_tarefa:int) -> int:

        sql = f"""UPDATE {self.__NOME_TABELA} SET status = 'F', finalizado_em = ? WHERE id_tarefa = ? AND status = 'A'"""

        data = date.today().strftime("%d/%m/%Y")
        resultado = self.executar_sql(sql, (data, id_tarefa), comitar=True).rowcount
        self.fechar_conexao()

        return resultado


    def selecionar_todas_tarefas(self, id_usuario: int) -> list:

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_usuario,)).fetchall()
        self.fechar_conexao()

        return resultado
    

    def selecionar_tarefa_por_id(self, id_tarefa: int) -> list:
        """ retorna id_usuario, descricao, importancia, status """

        sql = f"""SELECT id_usuario, descricao, importancia, status FROM {self.__NOME_TABELA} WHERE id_tarefa = ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_tarefa,)).fetchone()
        self.fechar_conexao()
        
        return resultado


    def selecionar_tarefas_por_status(self, id_usuario: int, status: str) -> list:
        """ retorna id_tarefa, descricao, importancia """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND status = ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_usuario, status)).fetchall()
        self.fechar_conexao()

        return resultado
    

    def selecionar_tarefas_por_importancia(self, id_usuario: int, importancia: str) -> list:
        """ retorna id_tarefa, descricao, importancia, status, criado_em, finalizado_em """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND importancia = ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_usuario, importancia)).fetchall()
        self.fechar_conexao()

        return resultado
    

    def selecionar_tarefas_por_data(self, tipo_data: str, id_usuario: int, data_inicio: str, data_final: str) -> list:
        """ retorna id_tarefa, descricao, importancia, status, criado_em, finalizado_em """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND {tipo_data} >= ? AND {tipo_data} <= ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_usuario, data_inicio, data_final)).fetchall()
        self.fechar_conexao()

        return resultado