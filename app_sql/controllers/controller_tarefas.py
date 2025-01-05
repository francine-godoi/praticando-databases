from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa

class ControllerTarefas:
    
    def adicionar_tarefa(self, usuario: tuple):
        print(f"Adicionada tarefa para o usuário {usuario[0]}- {usuario[1]}")

    def editar_tarefa(self, usuario: tuple):
        print(f"Editada a tarefa do usuário {usuario[0]}- {usuario[1]}")

    def excluir_tarefa(self, usuario: tuple):
        print(f"Excluída a tarefa do usuário {usuario[0]}- {usuario[1]}")

    def finalizar_tarefa(self, usuario: tuple):
        print(f"Finalizada a tarefa do usuário {usuario[0]}- {usuario[1]}")

    def listar_todas_tarefas(self, usuario: tuple):
        print(f"Listada todas as tarefas do usuário {usuario[0]}- {usuario[1]}")

    def listar_tarefas_andamento(self, usuario: tuple):
        print(f"Listada tarefas em andamento do usuário {usuario[0]}- {usuario[1]}")

    def listar_tarefas_finalizadas(self, usuario: tuple):
        print(f"Listada tarefas finalizadas do usuário {usuario[0]}- {usuario[1]}")

    def listar_tarefas_por_importancia(self, usuario: tuple):
        print(f"Listada tarefas por importância do usuário {usuario[0]}- {usuario[1]}")

    def listar_tarefas_por_criacao(self, usuario: tuple):
        print(f"Listada tarefas por data de criação do usuário {usuario[0]}- {usuario[1]}")

    def listar_tarefas_por_finalizacao(self, usuario: tuple):
        print(f"Listada tarefas por data de finalização do usuário {usuario[0]}- {usuario[1]}")