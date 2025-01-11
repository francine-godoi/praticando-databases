from datetime import datetime

from models.tarefas import Tarefa


class TelaTarefas:

    def mostrar_menu_tarefas(self, username: str) -> None:
        print(f"Bem Vindo, {username}!\nO que deseja fazer?\n")
        print("1. Adicionar Tarefa.")
        print("2. Editar Tarefa.")
        print("3. Excluir Tarefa.")
        print("4. Finalizar Tarefa.")
        print("5. Listar Tarefas.")
        print("6. Logout.\n")

    def mostrar_submenu_listar_tarefas(self) -> None:
        print("Listar: ")
        print("1. Todas as Tarefa.")
        print("2. Tarefas em andamento.")
        print("3. Tarefas finalizadas.")
        print("4. Por data.")
        print("5. Por importância.")
        print("6. Voltar.\n")

    def mostrar_submenu_listar_por_data(self) -> None:
        print("Listar por data de: ")
        print("1. Criação.")
        print("2. Finalização.")
        print("3. Voltar.\n")

    def mostrar_mensagem(self, mensagem) -> None:
        print(mensagem, "\n")

    def pegar_informacoes_para_adicionar_tarefa(self) -> tuple:
        # pede as informações para o usuário
        descricao = input("Descrição: ").strip()
        if descricao == "":
            self.mostrar_mensagem("Descrição não pode ficar em branco.")
            return (0, 0)

        importancia = ""
        while importancia not in ("A", "M", "B"):
            importancia = (
                input("Importância (A = Alta, M = Média, B = Baixa): ").strip().upper()
            )

        return (descricao, importancia)

    def pegar_informacoes_para_editar_tarefa(self, tarefa_selecionada: Tarefa) -> tuple:
        # mostra informações atuais para comparação
        print("\nInformações atuais: ")
        print(
            f"Descrição: {tarefa_selecionada.descricao} - Importância: {tarefa_selecionada.importancia}\n"
        )

        # pede as novas informações para o usuário
        nova_descricao = input(
            "Nova descrição: (Aperte Enter para não modificar): "
        ).strip()

        nova_importancia = None
        while nova_importancia not in ("A", "M", "B", ""):
            nova_importancia = (
                input(
                    "Importância: (A = Alta, M = Média, B = Baixa): (Aperte Enter para não modificar) "
                )
                .upper()
                .strip()
            )

        return (nova_descricao, nova_importancia)

    def pegar_id_tarefa_para_realizar_operacao(self, tarefas: list[Tarefa]) -> int:
        # verifica se o usuário quer ver a lista de tarefas e mostra para ele
        self.mostrar_tarefas_disponiveis_para_operacao(tarefas)
        # pede ao usuário para escolher um id
        id_tarefa = input("Qual o id da tarefa? ")
        try:  # verifica se id digitado é um número
            id_tarefa = int(id_tarefa)
        except ValueError:
            print("Id inválido.")
            return 0
        return int(id_tarefa)

    def mostrar_tarefas_disponiveis_para_operacao(self, tarefas: list[Tarefa]) -> None:
        # pergunta se o usuário quer ver as tarefas em andamento
        opcao = ""
        while opcao not in ("S", "N"):
            opcao = input("Deseja ver as tarefas em andamento? S/N ").strip().upper()

        # exibe a lista na tela
        if opcao == "S":
            for tarefa in tarefas:
                print(
                    f"Id: {tarefa.id_tarefa} - Descrição: {tarefa.descricao} - Importância: {tarefa.importancia}"
                )

    def pegar_importancia_para_filtragem(self) -> str:
        # pede ao usuário para escolher a importância da tarefa
        importancia = None
        while importancia not in ("A", "M", "B"):
            importancia = input(
                "Importância: (A = Alta, M = Média, B = Baixa): "
            ).upper().strip()
        return importancia

    def pegar_datas_para_filtragem(self) -> tuple:
        # pede para o usuário informar as datas para filtragem
        data_inicial = input("Data Inicial (dd/mm/aaaa): ").strip()
        data_final = input("Data Final (dd/mm/aaaa): ").strip()

        # verifica se o formato das datas está correto
        try:
            datetime.strptime(data_inicial, "%d/%m/%Y")
            datetime.strptime(data_final, "%d/%m/%Y")
        except ValueError:
            self.mostrar_mensagem("Data no formato errado. Tente novamente.")
            return (0, 0)

        return (data_inicial, data_final)

    def exibir_tarefas(self, tarefas: list[Tarefa]) -> None:

        print(
            "Id   Descrição                              Importância      Status           Criado     Finalizado"
        )
        opcoes = {"A": "Alta", "B": "Baixa", "M": "Média"}
        for tarefa in tarefas:
            importancia = ""
            if tarefa.importancia in opcoes:
                importancia = opcoes[tarefa.importancia]

            print(
                f"{tarefa.id_tarefa: <3}  {tarefa.descricao: <35}  {importancia: ^15}  {'Em andamento' if tarefa.status == 'A' else 'Finalizada': <15}  {tarefa.criado_em: <10} - {tarefa.finalizado_em if tarefa.finalizado_em is not None else '    -    ': <10}"
            )
        print("\n")
