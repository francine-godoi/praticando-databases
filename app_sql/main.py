from controllers.controller_menus import ControllerMenus
from repositories.repositorio_tarefas import RepositorioTarefa
from models.tarefas import Tarefa

if __name__ == "__main__":
    ControllerMenus().main()

    # t = Tarefa(1, "descricao alterada", "M", 4)
    # a = RepositorioTarefa().editar_tarefa(t)

    # if not a:
    #     print("nenhuma tarefa encontrada")
    # else:
    #     if isinstance(a, list):
    #         for x in a:
    #             print(x)