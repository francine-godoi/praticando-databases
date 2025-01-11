from models.tarefas import Tarefa
from repositories.auxiliar_db import AuxiliarDB
from datetime import date

class RepositorioTarefa(AuxiliarDB):

    __NOME_TABELA = "tarefas"
    __FOREIGN_TABELA = "usuarios"

    def __init__(self) -> None:
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
    

    def adicionar_tarefa(self, tarefa: Tarefa) -> int:

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

    
    def excluir_tarefa(self, id_tarefa:int) -> int:

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


    def selecionar_todas_tarefas(self, id_usuario: int) -> list[Tarefa]:

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? ORDER BY id_tarefa"""

        resultados = self.executar_sql(sql, (id_usuario,)).fetchall()
        self.fechar_conexao()

        lista_tarefas = lista_tarefas = self.criar_lista_de_tarefas(id_usuario, resultados)
        
        return lista_tarefas
    

    def selecionar_tarefa_por_id(self, id_tarefa: int, id_usuario: int) -> Tarefa:
        """ retorna id_usuario, descricao, importancia, status """

        sql = f"""SELECT id_usuario, descricao, importancia, status, id_tarefa FROM {self.__NOME_TABELA} WHERE id_tarefa = ? AND status = 'A' and id_usuario = ? ORDER BY id_tarefa"""

        resultado = self.executar_sql(sql, (id_tarefa, id_usuario)).fetchone()
        self.fechar_conexao()

        if not resultado:
            return 0
        
        tarefa = Tarefa(id_usuario, resultado[1], resultado[2], id_tarefa)
        
        return tarefa


    def selecionar_tarefas_por_status(self, id_usuario: int, status: str) -> list[Tarefa]:
        """ retorna id_tarefa, descricao, importancia """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND status = ? ORDER BY id_tarefa"""

        resultados = self.executar_sql(sql, (id_usuario, status)).fetchall()
        self.fechar_conexao()

        lista_tarefas = lista_tarefas = self.criar_lista_de_tarefas(id_usuario, resultados)
        
        return lista_tarefas
    

    def selecionar_tarefas_por_importancia(self, id_usuario: int, importancia: str) -> list[Tarefa]:
        """ retorna id_tarefa, descricao, importancia, status, criado_em, finalizado_em """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND importancia = ? ORDER BY id_tarefa"""

        resultados = self.executar_sql(sql, (id_usuario, importancia)).fetchall()
        self.fechar_conexao()

        lista_tarefas = lista_tarefas = self.criar_lista_de_tarefas(id_usuario, resultados)
        
        return lista_tarefas
    

    def selecionar_tarefas_por_data(self, tipo_data: str, id_usuario: int, data_inicio: str, data_final: str) -> list[Tarefa]:
        """ retorna id_tarefa, descricao, importancia, status, criado_em, finalizado_em """

        sql = f"""SELECT id_tarefa, descricao, importancia, status, criado_em, finalizado_em FROM {self.__NOME_TABELA} WHERE id_usuario = ? AND {tipo_data} >= ? AND {tipo_data} <= ? ORDER BY id_tarefa"""

        resultados = self.executar_sql(sql, (id_usuario, data_inicio, data_final)).fetchall()
        self.fechar_conexao()

        lista_tarefas = self.criar_lista_de_tarefas(id_usuario, resultados)
        
        return lista_tarefas
    

    def criar_lista_de_tarefas(self, id_usuario, resultados) -> list[Tarefa]:
        lista_tarefas = []
        for resultado in resultados:
            tarefa = Tarefa(id_usuario=id_usuario, id_tarefa=resultado[0], descricao=resultado[1], importancia=resultado[2], status=resultado[3], criado_em=resultado[4], finalizado_em=resultado[5])
            lista_tarefas.append(tarefa)
        
        return lista_tarefas