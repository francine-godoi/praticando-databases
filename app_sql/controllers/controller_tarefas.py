from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa
from views.tela_tarefas import TelaTarefas

class ControllerTarefas:

    def __init__(self, usuario: int):
        self.id_usuario = usuario
        self.repo_tarefa = RepositorioTarefa()
        self.tela_tarefas = TelaTarefas()
    

    def adicionar_tarefa(self) -> None:

        descricao = input("Descrição: ").strip()
        if descricao == "":
            print("Descrição não pode ficar em branco.\n")
            return self.adicionar_tarefa()
        
        importancia = ""
        while importancia not in ("A", "M", "B"):
            importancia = input("Importância (A = Alta, M = Média, B = Baixa): ").strip().upper()

        tarefa = Tarefa(self.id_usuario, descricao, importancia)
        cadastrado = self.repo_tarefa.cadastrar_tarefa(tarefa)
        if cadastrado:
            print("Tarefa cadastrada com sucesso.\n")            
        else:
            print("Não foi possível cadastar a tarefa.\n")            


    def editar_tarefa(self) -> None:

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.editar_tarefa()
        elif id_tarefa == -1: # Não tem tarefas para realizar operação
            return
        
        # TODO: arrumar select para pegar apenas campos necessarios
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(id_tarefa)

        print("Informações atuais: ")
        print(f"\nDescrição: {tarefa_selecionada[2]} - Importância: {tarefa_selecionada[3]}\n") 

        descricao = input("Nova descrição: (Aperte Enter para não modificar): ")  

        importancia = None
        while importancia not in ("A", "M", "B", ""):
            importancia = input("Importância: (A = Alta, M = Média, B = Baixa): (Aperte Enter para não modificar) ").upper()

        if descricao == "": 
            descricao = tarefa_selecionada[2]
        
        if importancia == "":
            importancia = tarefa_selecionada[3]

        tarefa = Tarefa(self.id_usuario, descricao, importancia, id_tarefa)

        editado = self.repo_tarefa.editar_tarefa(tarefa)
        if editado:
            print("Tarefa editada com sucesso!\n")            
        else:
            print("Não foi possível editar a tarefa.\n")            


    def excluir_tarefa(self) -> None:

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.excluir_tarefa()
        elif id_tarefa == -1: # Não tem tarefas para realizar operação
            return

        deletado = self.repo_tarefa.deletar_tarefa(id_tarefa)
        if deletado:
            print("Tarefa excluida com sucesso.\n")                        
        else:
            print("Não foi possível excluir a tarefa.\n")                               
        

    def finalizar_tarefa(self) -> None:

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.finalizar_tarefa()
        elif id_tarefa == -1: # Não tem tarefas para realizar operação
            return
        
        finalizada = self.repo_tarefa.finalizar_tarefa(id_tarefa)
        if finalizada:
            print("Tarefa finalizada com sucesso.\n")            
        else:
            print("Não foi possível finalizar a tarefa.\n")            


    def pegar_id_tarefa(self) -> int:
        # TODO: arrumar select para pegar apenas campos necessarios
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        if not tarefas:
            print("Usuario não tem tarefas para realizar a operação.\n")
            return -1
        
        opcao = ""
        while opcao not in ("S", "N"):
            opcao = input("Deseja ver as tarefas em andamento? S/N ").strip().upper()

        # TODO: FORMATAR A EXIBIÇÃO DAS INFORMAÇÕES, USAR VIEWS PARA EXIBIR 
        if opcao == "S":                        
            for tarefa in tarefas:
                print(tarefa)

        id_tarefa = input("Qual o id da tarefa? ")
        # TODO: arrumar select para pegar apenas campos necessarios
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(id_tarefa)

        if not tarefa_selecionada:
            print("Tarefa não cadastrada.\n")
            return 0

        if tarefa_selecionada[1] != self.id_usuario:
            print("Tarefa não pertence ao usuário.\n")
            return 0
        
        if tarefa_selecionada[4] != "A":
            print("Essa tarefa já foi finalizada.\n")
            return 0
        
        return id_tarefa

    # TODO: arrumar select para pegar apenas campos necessarios
    def listar_todas_tarefas(self) -> None:
        resultado = self.repo_tarefa.selecionar_todas_tarefas()
        self.tela_tarefas.exibir_tarefas(resultado)

    # TODO: arrumar select para pegar apenas campos necessarios
    def listar_tarefas_em_andamento(self) -> None:
        resultado = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        self.tela_tarefas.exibir_tarefas(resultado)

    # TODO: arrumar select para pegar apenas campos necessarios
    def listar_tarefas_finalizadas(self) -> None:
        resultado = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "F")
        self.tela_tarefas.exibir_tarefas(resultado)

    # TODO: arrumar select para pegar apenas campos necessarios
    def listar_tarefas_por_importancia(self, importancia: str) -> None:
        resultado = self.repo_tarefa.selecionar_tarefas_por_importancia(self.id_usuario, importancia)
        self.tela_tarefas.exibir_tarefas(resultado)

    # TODO: fazer
    def listar_tarefas_por_criacao(self) -> None:
        print(f"Listada tarefas por data de criação do usuário {self.id_usuario}")

    # TODO: fazer
    def listar_tarefas_por_finalizacao(self) -> None:
        print(f"Listada tarefas por data de finalização do usuário {self.id_usuario}")