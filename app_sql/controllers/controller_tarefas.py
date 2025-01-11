from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa
from views.tela_tarefas import TelaTarefas


class ControllerTarefas:

    def __init__(self, id_usuario: int) -> None:
        # Vincula a tarefa com o usuário logado
        self.id_usuario = id_usuario
        self.repo_tarefa = RepositorioTarefa()
        self.tela_tarefas = TelaTarefas()

    def adicionar_tarefa(self) -> None:
        # chama o método que coleta as informações do usuário
        descricao, importancia = (
            self.tela_tarefas.pegar_informacoes_para_adicionar_tarefa()
        )
        if not descricao:
            return self.adicionar_tarefa()

        nova_tarefa = Tarefa(self.id_usuario, descricao, importancia)

        # salva os dados no banco
        cadastrado = self.repo_tarefa.adicionar_tarefa(nova_tarefa)
        if cadastrado:
            self.tela_tarefas.mostrar_mensagem("Tarefa cadastrada com sucesso.")
        else:
            self.tela_tarefas.mostrar_mensagem("Não foi possível cadastar a tarefa.")

    def editar_tarefa(self) -> None:
        # pega a tarefa a ser editada
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()
        if not tarefa_selecionada:
            return self.editar_tarefa()

        # pega novas informações com usuário
        nova_descricao, nova_importancia = (
            self.tela_tarefas.pegar_informacoes_para_editar_tarefa(tarefa_selecionada)
        )

        # se usuário pressionou enter as informação permanecem sem alteração
        if nova_descricao == "":
            nova_descricao = tarefa_selecionada.descricao

        if nova_importancia == "":
            nova_importancia = tarefa_selecionada.importancia

        # cria uma tarefa com as informações editadas
        tarefa = Tarefa(
            self.id_usuario,
            nova_descricao,
            nova_importancia,
            tarefa_selecionada.id_tarefa,
        )

        # salva a edição no banco
        editado = self.repo_tarefa.editar_tarefa(tarefa)
        if editado:
            self.tela_tarefas.mostrar_mensagem("Tarefa editada com sucesso!")
        else:
            self.tela_tarefas.mostrar_mensagem("Não foi possível editar a tarefa.")

    def excluir_tarefa(self) -> None:
        # pega a tarefa a ser excluída
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()
        if not tarefa_selecionada:
            return self.excluir_tarefa()

        # deleta tarefa do banco
        deletado = self.repo_tarefa.excluir_tarefa(tarefa_selecionada)
        if deletado:
            self.tela_tarefas.mostrar_mensagem("Tarefa excluída com sucesso.")
        else:
            self.tela_tarefas.mostrar_mensagem("Não foi possível excluir a tarefa.")

    def finalizar_tarefa(self) -> None:
        # pega a tarefa a ser finalizada
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()
        if not tarefa_selecionada:
            return self.finalizar_tarefa()

        # altera as informações no banco para demostrar a finalização da tarefa
        finalizada = self.repo_tarefa.finalizar_tarefa(tarefa_selecionada)
        if finalizada:
            self.tela_tarefas.mostrar_mensagem("Tarefa finalizada com sucesso.")
        else:
            self.tela_tarefas.mostrar_mensagem("Não foi possível finalizar a tarefa.")

    def pegar_tarefa_para_realizar_operacao(self) -> Tarefa | int:
        # só é possível realizar operações (editar,excluir,finalizar) em tarefas em andamento
        if not self.existe_tarefas_em_andamento():
            return 0

        # pega as tarefas do usuário disponíveis para operação
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        # envia tarefas disponíveis e pega o id da tarefa desejada com o usuário
        id_tarefa = self.tela_tarefas.pegar_id_tarefa_para_realizar_operacao(tarefas)
        if not id_tarefa:
            return 0

        # busca a tarefa no banco pelo id selecionado, já verificando se ela pertence ao usuário
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(
            id_tarefa, self.id_usuario
        )
        if not tarefa_selecionada:
            self.tela_tarefas.mostrar_mensagem(
                "Não foi possível selecionar a tarefa. Favor consultar a tabela."
            )
            return 0

        return tarefa_selecionada

    def existe_tarefas_em_andamento(self) -> bool:
        # verifica se o usuário tem tarefas com status 'A' = Andamento
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        if not tarefas:
            self.tela_tarefas.mostrar_mensagem(
                "Usuário não tem tarefas para realizar a operação."
            )
            return False
        return True

    def listar_todas_tarefas(self) -> None:
        # pega todas as tarefas do usuário e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_todas_tarefas(self.id_usuario)
        if not tarefas:
            self.tela_tarefas.mostrar_mensagem("Nenhuma tarefa encontrada.")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_status(self, tipo_status: str) -> None:
        """Tipo status: 'A' = Andamento ou 'F' = Finalizado."""
        # pega as tarefas do usuário conforme status selecionado e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(
            self.id_usuario, tipo_status
        )
        if not tarefas:
            self.tela_tarefas.mostrar_mensagem("Nenhuma tarefa encontrada.")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_importancia(self) -> None:
        # pede para o usuário escolher a importância das tarefas que deseja visualizar
        importancia = self.tela_tarefas.pegar_importancia_para_filtragem()
        # pega as tarefas do usuário conforme importância selecionada e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_importancia(
            self.id_usuario, importancia
        )
        if not tarefas:
            self.tela_tarefas.mostrar_mensagem("Nenhuma tarefa encontrada.")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)

    def listar_tarefas_por_data(self, tipo_data: str) -> None:
        """Tipo data = 'criado_em' ou 'finalizado_em'."""
        # pede para o usuário escolher as datas para filtragem
        data_inicial, data_final = self.tela_tarefas.pegar_datas_para_filtragem()
        if not data_inicial or not data_final:
            return self.listar_tarefas_por_data(tipo_data)

        # pega as tarefas do usuário entre as datas escolhidas e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_data(
            tipo_data, self.id_usuario, data_inicial, data_final
        )
        if not tarefas:
            self.tela_tarefas.mostrar_mensagem("Nenhuma tarefa encontrada.")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)
