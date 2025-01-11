from models.tarefas import Tarefa

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


    def exibir_tarefas(self, tarefas: list[Tarefa]) -> None:
        
        print("Id   Descrição                              Importância      Status           Criado     Finalizado")
        opcoes = {"A": "Alta", "B": "Baixa", "M": "Média"}
        for tarefa in tarefas:
            importancia = ""
            if tarefa.importancia in opcoes:
                importancia = opcoes[tarefa.importancia]

            print(f"{tarefa.id_tarefa: <3}  {tarefa.descricao: <35}  {importancia: ^15}  {'Em andamento' if tarefa.status == 'A' else 'Finalizada': <15}  {tarefa.criado_em: <10} - {tarefa.finalizado_em if tarefa.finalizado_em is not None else '    -    ': <10}")
        print("\n")