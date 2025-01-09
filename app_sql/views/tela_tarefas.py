class TelaTarefas:

    def mostrar_menu_tarefas(self, username:str) -> None:
        
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


    def exibir_tarefas(self, tarefas) -> None:
        
        print("Id   Descrição                              Importância      Status           Criado     Finalizado")
        opcoes = {"A": "Alta", "B": "Baixa", "M": "Média"}
        for tarefa in tarefas:
            importancia = ""
            if tarefa[2] in opcoes:
                importancia = opcoes[tarefa[2]]

            print(f"{tarefa[0]: <3}  {tarefa[1]: <35}  {importancia: ^15}  {'Em andamento' if tarefa[3] == 'A' else 'Finalizada': <15}  {tarefa[4]: <10} - {tarefa[5] if tarefa[5] is not None else '    -    ': <10}")
        print("\n")