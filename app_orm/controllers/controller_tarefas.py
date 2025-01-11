from datetime import datetime

from models.tarefas import Tarefa
from utils.conexao_db import session
from views.tela_tarefas import TelaTarefas


class ControllerTarefas:

    def __init__(self, usuario: int):
        self.id_usuario = usuario
        self.tela_tarefas = TelaTarefas()

    def adicionar_tarefa(self) -> None:
        descricao = input("Descrição: ").strip()
        if descricao == "":
            print("Descrição não pode ficar em branco.\n")
            return self.adicionar_tarefa()

        importancia = ""
        while importancia not in ("A", "M", "B"):
            importancia = (
                input("Importância (A = Alta, M = Média, B = Baixa): ").strip().upper()
            )

        tarefa = Tarefa(
            self.id_usuario,
            descricao,
            importancia,
            datetime.today().strftime("%d/%m/%Y"),
        )
        try:
            session.add(tarefa)
            session.commit()
            print("Tarefa cadastrada com sucesso.\n")
        except Exception as e:
            session.rollback()
            print(f"Não foi possível cadastrar a tarefa. Um erro ocorreu: {e}\n")

    def editar_tarefa(self) -> None:
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        tarefa_selecionada = self.selecionar_tarefa_por_id()
        if tarefa_selecionada == 0:  # id inválida
            return self.editar_tarefa()

        print("\nInformações atuais: ")
        print(
            f"Descrição: {tarefa_selecionada.descricao} - Importância: {tarefa_selecionada.importancia}\n"
        )

        descricao = input("Nova descrição: (Aperte Enter para não modificar): ")

        importancia = None
        while importancia not in ("A", "M", "B", ""):
            importancia = input(
                "Importância: (A = Alta, M = Média, B = Baixa): (Aperte Enter para não modificar) "
            ).upper()

        if descricao != "":
            tarefa_selecionada.descricao = descricao

        if importancia != "":
            tarefa_selecionada.importancia = importancia

        try:
            session.add(tarefa_selecionada)
            session.commit()
            print("Tarefa editada com sucesso!\n")
        except Exception as e:
            session.rollback()
            print(f"Não foi possível editar a tarefa. Um erro ocorreu: {e}\n")

    def excluir_tarefa(self) -> None:
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        tarefa_selecionada = self.selecionar_tarefa_por_id()
        if tarefa_selecionada == 0:  # id inválida
            return self.excluir_tarefa()

        try:
            session.delete(tarefa_selecionada)
            session.commit()
            print("Tarefa excluida com sucesso.\n")
        except Exception as e:
            session.rollback()
            print(f"Não foi possível excluir a tarefa. Um erro ocorreu: {e}\n")

    def finalizar_tarefa(self) -> None:
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        tarefa_selecionada = self.selecionar_tarefa_por_id()
        if tarefa_selecionada == 0:  # id inválida
            return self.finalizar_tarefa()

        tarefa_selecionada.finalizado_em = datetime.today().strftime("%d/%m/%Y")
        tarefa_selecionada.status = "F"
        try:
            session.add(tarefa_selecionada)
            session.commit()
            print("Tarefa finalizada com sucesso.\n")
        except Exception as e:
            session.rollback()
            print(f"Não foi possível  finalizar a tarefa. Um erro ocorreu: {e}\n")

    def existe_tarefas_andamento(self) -> bool:
        tarefas = (
            session.query(Tarefa)
            .filter(Tarefa.id_usuario == self.id_usuario)
            .where(Tarefa.status == "A")
            .all()
        )
        if not tarefas:
            print("Usuario não tem tarefas para realizar a operação.\n")
            return False
        return True

    def motrar_tarefas_andamento(self) -> None:
        opcao = ""
        while opcao not in ("S", "N"):
            opcao = input("Deseja ver as tarefas em andamento? S/N ").strip().upper()

        if opcao == "S":
            tarefas = (
                session.query(Tarefa)
                .filter(Tarefa.id_usuario == self.id_usuario)
                .where(Tarefa.status == "A")
                .all()
            )
            for tarefa in tarefas:
                print(
                    f"Id: {tarefa.id_tarefa} - Descrição: {tarefa.descricao} - Importância: {tarefa.importancia}"
                )

    def selecionar_tarefa_por_id(self) -> int | Tarefa:
        id_tarefa = input("Qual o id da tarefa? ")
        tarefa_selecionada = (
            session.query(Tarefa)
            .filter(Tarefa.id_tarefa == id_tarefa)
            .where(Tarefa.status == "A")
            .where(Tarefa.id_usuario == self.id_usuario)
            .first()
        )

        if not tarefa_selecionada:
            print("Não foi possível selecionar a tarefa. Favor verificar a lista.\n")
            return 0

        return tarefa_selecionada

    def listar_todas_tarefas(self) -> None:
        tarefas = (
            session.query(Tarefa).filter(Tarefa.id_usuario == self.id_usuario).all()
        )
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_status(self, tipo_status: str) -> None:
        tarefas = (
            session.query(Tarefa)
            .filter(Tarefa.id_usuario == self.id_usuario)
            .where(Tarefa.status == tipo_status)
            .all()
        )
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_importancia(self) -> None:
        importancia = None
        while importancia not in ("A", "M", "B"):
            importancia = input(
                "Importância: (A = Alta, M = Média, B = Baixa): "
            ).upper()

        tarefas = (
            session.query(Tarefa)
            .filter(Tarefa.id_usuario == self.id_usuario)
            .where(Tarefa.importancia == importancia)
            .all()
        )
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_data(self, tipo_data: str) -> None:
        data_inicial = input("Data Inicial (dd/mm/aaaa): ").strip()
        data_final = input("Data Final (dd/mm/aaaa): ").strip()

        try:
            datetime.strptime(data_inicial, "%d/%m/%Y")
            datetime.strptime(data_final, "%d/%m/%Y")
        except ValueError:
            print("Data no formato errado. Tente novamente.\n")
            return self.listar_tarefas_por_data(tipo_data)

        if tipo_data == "criado_em":
            tarefas = (
                session.query(Tarefa)
                .filter(Tarefa.id_usuario == self.id_usuario)
                .where(Tarefa.criado_em >= data_inicial)
                .where(Tarefa.criado_em <= data_final)
            )
        elif tipo_data == "finalizado_em":
            tarefas = (
                session.query(Tarefa)
                .filter(Tarefa.id_usuario == self.id_usuario)
                .where(Tarefa.finalizado_em >= data_inicial)
                .where(Tarefa.finalizado_em <= data_final)
            )

        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)
