from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa
from views.tela_tarefas import TelaTarefas

from datetime import datetime

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
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.editar_tarefa()
        
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(id_tarefa)

        print("\nInformações atuais: ")
        print(f"Descrição: {tarefa_selecionada[1]} - Importância: {tarefa_selecionada[2]}\n") 

        descricao = input("Nova descrição: (Aperte Enter para não modificar): ")  

        importancia = None
        while importancia not in ("A", "M", "B", ""):
            importancia = input("Importância: (A = Alta, M = Média, B = Baixa): (Aperte Enter para não modificar) ").upper()

        if descricao == "": 
            descricao = tarefa_selecionada[1]
        
        if importancia == "":
            importancia = tarefa_selecionada[2]

        tarefa = Tarefa(self.id_usuario, descricao, importancia, id_tarefa)

        editado = self.repo_tarefa.editar_tarefa(tarefa)
        if editado:
            print("Tarefa editada com sucesso!\n")            
        else:
            print("Não foi possível editar a tarefa.\n")            


    def excluir_tarefa(self) -> None:
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.excluir_tarefa()

        deletado = self.repo_tarefa.deletar_tarefa(id_tarefa)
        if deletado:
            print("Tarefa excluida com sucesso.\n")                        
        else:
            print("Não foi possível excluir a tarefa.\n")                               
        

    def finalizar_tarefa(self) -> None:
        if not self.existe_tarefas_andamento():
            return

        self.motrar_tarefas_andamento()

        id_tarefa = self.pegar_id_tarefa()
        if id_tarefa == 0: # id inválida
            return self.finalizar_tarefa()
        
        finalizada = self.repo_tarefa.finalizar_tarefa(id_tarefa)
        if finalizada:
            print("Tarefa finalizada com sucesso.\n")            
        else:
            print("Não foi possível finalizar a tarefa.\n")            


    def existe_tarefas_andamento(self) -> bool:
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        if not tarefas:
            print("Usuario não tem tarefas para realizar a operação.\n")
            return False
        return True


    def motrar_tarefas_andamento(self) -> None:       
        opcao = ""
        while opcao not in ("S", "N"):
            opcao = input("Deseja ver as tarefas em andamento? S/N ").strip().upper()

        if opcao == "S":
            tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")                        
            for tarefa in tarefas:
                print(f"Id: {tarefa[0]} - Descrição: {tarefa[1]} - Importância: {tarefa[2]}")


    def pegar_id_tarefa(self) -> int:
        id_tarefa = input("Qual o id da tarefa? ")
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(id_tarefa)

        if not tarefa_selecionada:
            print("Tarefa não cadastrada.\n")
            return 0

        if tarefa_selecionada[0] != self.id_usuario:
            print("Tarefa não pertence ao usuário.\n")
            return 0
        
        if tarefa_selecionada[3] != "A":
            print("Essa tarefa já foi finalizada.\n")
            return 0
        
        return id_tarefa


    def listar_todas_tarefas(self) -> None:
        tarefas = self.repo_tarefa.selecionar_todas_tarefas(self.id_usuario)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def listar_tarefas_por_status(self, tipo_status: str) -> None:
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, tipo_status)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def listar_tarefas_por_importancia(self) -> None:        
        importancia = None
        while importancia not in ("A", "M", "B"):
            importancia = input("Importância: (A = Alta, M = Média, B = Baixa): ").upper()
            
        tarefas = self.repo_tarefa.selecionar_tarefas_por_importancia(self.id_usuario, importancia)
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

        tarefas = self.repo_tarefa.selecionar_tarefas_por_data(tipo_data, self.id_usuario, data_inicial, data_final)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)