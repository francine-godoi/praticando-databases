from datetime import datetime
from models.tarefas import Tarefa
from database.conexao_db import ConexaoDb
from sqlalchemy import literal_column
from models.base import Base


class RepositorioTarefa:

    def __init__(self) -> None:
        self.conexao = ConexaoDb()
        self.session = self.conexao.criar_session()
        self.criar_tabela_tarefas()

    def criar_tabela_tarefas(self) -> None:
        Base.metadata.create_all(bind=self.conexao.db)

    def adicionar_tarefa(self, tarefa: Tarefa) -> int:
        try:
            self.session.add(tarefa)
            self.session.commit()
            self.session.close()
            return 1
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print(f"Não foi possível cadastrar a tarefa. Um erro ocorreu: {e}\n")
            return 0

    def editar_tarefa(self, novos_dados: dict) -> int:
        tarefa_selecionada: Tarefa = self.selecionar_tarefa_por_id(
                                            novos_dados['id_tarefa'],
                                            novos_dados['id_usuario']
                                            )

        tarefa_selecionada.descricao = novos_dados['descricao']
        tarefa_selecionada.importancia = novos_dados['importancia']
        try:
            self.session.add(tarefa_selecionada)
            self.session.commit()
            self.session.close()
            return 1
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print(f"Não foi possível editar a tarefa. Um erro ocorreu: {e}\n")
            return 0

    def excluir_tarefa(self, tarefa: Tarefa) -> int:
        try:
            self.session.delete(tarefa)
            self.session.commit()
            self.session.close()
            return 1
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print(f"Não foi possível excluir a tarefa. Um erro ocorreu: {e}\n")
            return 0

    def finalizar_tarefa(self, tarefa: Tarefa) -> int:
        tarefa.status = "F"
        tarefa.finalizado_em = datetime.today().strftime("%d/%m/%Y")

        try:
            self.session.add(tarefa)
            self.session.commit()
            self.session.close()
            return 1
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print(f"Não foi possível finalizar a tarefa. Um erro ocorreu: {e}\n")

    def selecionar_todas_tarefas(self, id_usuario: int) -> list[Tarefa]:
        tarefas = (
            self.session.query(Tarefa).filter(
                Tarefa.id_usuario == id_usuario)
                .all()
        )
        self.session.close()
        return tarefas

    def selecionar_tarefa_por_id(self, id_tarefa: int, id_usuario: int) -> Tarefa:
        tarefa = (
            self.session.query(Tarefa).filter(
                Tarefa.id_usuario == id_usuario,
                Tarefa.id_tarefa == id_tarefa,
                Tarefa.status == 'A')
                .first()
        )
        self.session.close()
        return tarefa
        
    def selecionar_tarefas_por_status(
        self, id_usuario: int, status: str
    ) -> list[Tarefa]:
        
        tarefas = (
            self.session.query(Tarefa).filter(
                Tarefa.id_usuario == id_usuario,
                Tarefa.status == status)
                .all()
        )
        self.session.close()
        return tarefas
    
    def selecionar_tarefas_por_importancia(
        self, id_usuario: int, importancia: str
    ) -> list[Tarefa]:       
        
        tarefas = (
            self.session.query(Tarefa).filter(
                Tarefa.id_usuario == id_usuario,
                Tarefa.importancia == importancia)
                .all()
        )
        self.session.close()
        return tarefas        

    def selecionar_tarefas_por_data(
        self, tipo_data: str, id_usuario: int, data_inicio: str, data_final: str
    ) -> list[Tarefa]:
        
        tarefas = (
            self.session.query(Tarefa).filter(
                Tarefa.id_usuario == id_usuario,
                literal_column(tipo_data) >= data_inicio,
                literal_column(tipo_data) <= data_final)
                .all()
        )
        self.session.close()
        return tarefas