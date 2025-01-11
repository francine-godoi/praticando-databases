from models.tarefas import Tarefa
from repositories.repositorio_tarefas import RepositorioTarefa
from views.tela_tarefas import TelaTarefas

from datetime import datetime

class ControllerTarefas:

    def __init__(self, id_usuario: int) -> None:
        # Vincula a tarefa com o usuário logado
        self.id_usuario = id_usuario
        self.repo_tarefa = RepositorioTarefa()
        self.tela_tarefas = TelaTarefas()
    

    def adicionar_tarefa(self) -> None:
        # chama a função que coleta as informações do usuário
        informacao = self.pegar_informacao_para_adicionar_tarefa()    
        if not informacao:
            return self.adicionar_tarefa()   

        # salva os dados no banco
        cadastrado = self.repo_tarefa.adicionar_tarefa(informacao)
        if cadastrado:
            print("Tarefa cadastrada com sucesso.\n")            
        else:
            print("Não foi possível cadastar a tarefa.\n")            


    def pegar_informacao_para_adicionar_tarefa(self) -> Tarefa | int:
        # pede as informações para o usuário
        descricao = input("Descrição: ").strip()
        if descricao == "":
            print("Descrição não pode ficar em branco.\n")
            return 0
        
        importancia = ""
        while importancia not in ("A", "M", "B"):
            importancia = input("Importância (A = Alta, M = Média, B = Baixa): ").strip().upper()

        tarefa = Tarefa(self.id_usuario, descricao, importancia)

        return tarefa
    

    def editar_tarefa(self) -> None:
        # chama a função que coleta as informações do usuário
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()      
        if not tarefa_selecionada:
            return self.editar_tarefa()   

        nova_informacao = self.pegar_informacao_para_editar_tarefa(tarefa_selecionada)           

        # salva a edição no banco
        editado = self.repo_tarefa.editar_tarefa(nova_informacao)
        if editado:
            print("Tarefa editada com sucesso!\n")            
        else:
            print("Não foi possível editar a tarefa.\n")            


    def pegar_informacao_para_editar_tarefa(self, tarefa_selecionada: Tarefa) -> Tarefa:
        # mostra informações atuais para comparação
        print("\nInformações atuais: ")
        print(f"Descrição: {tarefa_selecionada.descricao} - Importância: {tarefa_selecionada.importancia}\n") 

        nova_descricao = input("Nova descrição: (Aperte Enter para não modificar): ")  

        nova_importancia = None
        while nova_importancia not in ("A", "M", "B", ""):
            nova_importancia = input("Importância: (A = Alta, M = Média, B = Baixa): (Aperte Enter para não modificar) ").upper()

        # caso o usuário pressionou enter as informações não serão editadas
        if nova_descricao == "": 
            nova_descricao = tarefa_selecionada.descricao
        
        if nova_importancia == "":
            nova_importancia = tarefa_selecionada.importancia

        tarefa = Tarefa(self.id_usuario, nova_descricao, nova_importancia, tarefa_selecionada.id_tarefa)

        return tarefa


    def excluir_tarefa(self) -> None:
        # chama a função que coleta as informações do usuário
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()  
        if not tarefa_selecionada: # id inválida
            return self.excluir_tarefa()

        # deleta tarefa do banco
        deletado = self.repo_tarefa.excluir_tarefa(tarefa_selecionada.id_tarefa)
        if deletado:
            print("Tarefa excluida com sucesso.\n")                        
        else:
            print("Não foi possível excluir a tarefa.\n")                               
        

    def finalizar_tarefa(self) -> None:
        # chama a função que coleta as informações do usuário
        tarefa_selecionada = self.pegar_tarefa_para_realizar_operacao()  
        if not tarefa_selecionada: # id inválida
            return self.finalizar_tarefa()
        
        # altera as informações no banco para mostrar a finalização da tarefa
        finalizada = self.repo_tarefa.finalizar_tarefa(tarefa_selecionada.id_tarefa)
        if finalizada:
            print("Tarefa finalizada com sucesso.\n")            
        else:
            print("Não foi possível finalizar a tarefa.\n")            


    def pegar_tarefa_para_realizar_operacao(self) -> Tarefa | int:
        # só é possível realizar operações em tarefas em andamento
        if not self.existe_tarefas_em_andamento():
            return 0

        # mostra tarefas que podem ser utilizadas na operação
        self.motrar_tarefas_em_andamento()

        # chama função que pede para o usuário escolher o id da tarefa
        tarefa_selecionada = self.selecionar_tarefa_por_id()
        if not tarefa_selecionada: # id inválida
            return 0
        
        return tarefa_selecionada


    def existe_tarefas_em_andamento(self) -> bool:
        # tenta selecionar todas as tarefas do banco que tenham status 'A' = Andamento
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")
        if not tarefas:
            print("Usuario não tem tarefas para realizar a operação.\n")
            return False
        return True


    def motrar_tarefas_em_andamento(self) -> None: 
        # pergunta se o usuário quer ver as tarefas em andamento      
        opcao = ""
        while opcao not in ("S", "N"):
            opcao = input("Deseja ver as tarefas em andamento? S/N ").strip().upper()

        # exibe a lista na tela
        if opcao == "S":
            tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, "A")                        
            for tarefa in tarefas:
                print(f"Id: {tarefa.id_tarefa} - Descrição: {tarefa.descricao} - Importância: {tarefa.importancia}")


    def selecionar_tarefa_por_id(self) -> Tarefa | int:
        
        id_tarefa = self.pegar_id_tarefa()
        if not id_tarefa:
            return 0
        
        # busca a tarefa referente ao id no banco
        tarefa_selecionada = self.repo_tarefa.selecionar_tarefa_por_id(id_tarefa, self.id_usuario)

        if not tarefa_selecionada:
            print("Não foi possível selecionar a tarefa. Favor consultar a tabela.\n")
            return 0
        
        return tarefa_selecionada
    

    def pegar_id_tarefa(self) -> int:
        # pede ao usuário para escolher um id
        id_tarefa = input("Qual o id da tarefa? ")
        try:
            id_tarefa = int(id_tarefa)
        except ValueError:
            print('Id inválido.')
            return 0
        return id_tarefa


    def listar_todas_tarefas(self) -> None:
        # pega todas as tarefas do banco e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_todas_tarefas(self.id_usuario)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def listar_tarefas_por_status(self, tipo_status: str) -> None:
        """ Tipo status: 'A' = Andamento ou 'F' = Finalizado. """
        # pega todas as tarefas em andamento do banco e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_status(self.id_usuario, tipo_status)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def listar_tarefas_por_importancia(self) -> None:  

        importancia = self.pegar_importancia()            
        # pega as informações do banco e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_importancia(self.id_usuario, importancia)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def pegar_importancia(self) -> str:
        # pede ao usuário para escolher a importancia da tarefa
        importancia = None
        while importancia not in ("A", "M", "B"):
            importancia = input("Importância: (A = Alta, M = Média, B = Baixa): ").upper()
        return importancia


    def listar_tarefas_por_data(self, tipo_data: str) -> None:
        """ Tipo data = 'criado_em' ou 'finalizado_em'. """
        data_inicial, data_final = self.pegar_data_para_filtrage()
        if not data_final:
            return self.listar_tarefas_por_data(tipo_data)
                
        # pega todas as tarefas do banco entre as datas escolhidas e envia para a view para exibição
        tarefas = self.repo_tarefa.selecionar_tarefas_por_data(tipo_data, self.id_usuario, data_inicial, data_final)
        if not tarefas:
            print("Nenhuma tarefa encontrada.\n")
            return
        self.tela_tarefas.exibir_tarefas(tarefas)


    def pegar_data_para_filtrage(self) -> tuple:
        # pede para o usuário informar as datas para filtragem
        data_inicial = input("Data Inicial (dd/mm/aaaa): ").strip()
        data_final = input("Data Final (dd/mm/aaaa): ").strip()

        # verifica se o formato das datas está correto
        try:
            datetime.strptime(data_inicial, "%d/%m/%Y")
            datetime.strptime(data_final, "%d/%m/%Y")
        except ValueError:
            print("Data no formato errado. Tente novamente.\n")
            return (0,0)
        
        return (data_inicial, data_final)