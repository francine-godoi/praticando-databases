from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa

class ControllerTarefas:

    def __init__(self, usuario:int):
        self.id_usuario = usuario
        self.repo_tarefa = RepositorioTarefa
    
    def adicionar_tarefa(self):
        print(f"Adicionada tarefa para o usuário {self.id_usuario}")

    def editar_tarefa(self):
        print(f"Editada a tarefa do usuário {self.id_usuario}")

    def excluir_tarefa(self):
        print(f"Excluída a tarefa do usuário {self.id_usuario}")

    def finalizar_tarefa(self):
        print(f"Finalizada a tarefa do usuário {self.id_usuario}")

    def listar_todas_tarefas(self):
        print(f"Listada todas as tarefas do usuário {self.id_usuario}")

    def listar_tarefas_andamento(self):
        print(f"Listada tarefas em andamento do usuário {self.id_usuario}")

    def listar_tarefas_finalizadas(self):
        print(f"Listada tarefas finalizadas do usuário {self.id_usuario}")

    def listar_tarefas_por_importancia(self):
        print(f"Listada tarefas por importância do usuário {self.id_usuario}")

    def listar_tarefas_por_criacao(self):
        print(f"Listada tarefas por data de criação do usuário {self.id_usuario}")

    def listar_tarefas_por_finalizacao(self):
        print(f"Listada tarefas por data de finalização do usuário {self.id_usuario}")