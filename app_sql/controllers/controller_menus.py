from controllers.controller_usuarios import ControllerUsuarios
from controllers.controller_tarefas import ControllerTarefas
from views.tela_inicial import TelaInicial
from views.tela_tarefas import TelaTarefas

class ControllerMenus:

    def __init__(self):
        self.tela_inicial = TelaInicial()
        self.tela_tarefas = TelaTarefas()
        self.ctrl_usuario = ControllerUsuarios()
        self.ctrl_tarefa = None
        self.usuario_logado = False


    def mostrar_menu_inicial(self) -> None:
        self.tela_inicial.mostrar_menu_inicial()


    def mostrar_menu_tarefas(self) -> None:        
        self.tela_tarefas.mostrar_menu_tarefas(self.usuario_logado)


    def tratar_opcao_menu_inicial(self, escolha: str) -> None:

        match escolha:
            case "1":
                self.ctrl_usuario.cadastrar_usuario()
            case "2":
                usuario_logado = self.ctrl_usuario.validar_credenciais()                
                if usuario_logado:                    
                    self.usuario_logado = usuario_logado[1] # username
                    self.ctrl_tarefa = ControllerTarefas(usuario_logado[0]) # id_usuario
            case "3":
                print("Tchau!!")
                exit()
            case _:
                print("Opção inválida.\n")                
            

    def tratar_opcao_menu_tarefas(self, escolha: str) -> None:
        match escolha:
            case "1":
                self.ctrl_tarefa.adicionar_tarefa()
            case "2":
                self.ctrl_tarefa.editar_tarefa()
            case "3":
                self.ctrl_tarefa.excluir_tarefa()
            case "4":
                self.ctrl_tarefa.finalizar_tarefa()
            case "5":
                self.tratar_opcao_submenu_listar_tarefas()
            case "6":
                self.usuario_logado = False
                self.main()
            case _:
                print("Opção inválida.\n")
                

    def tratar_opcao_submenu_listar_tarefas(self) -> None:
        self.tela_tarefas.mostrar_submenu_listar_tarefas()
        escolha = input()

        match escolha:
            case "1":
                self.ctrl_tarefa.listar_todas_tarefas()
            case "2":
                self.ctrl_tarefa.listar_tarefas_em_andamento()
            case "3":
                self.ctrl_tarefa.listar_tarefas_finalizadas()
            case "4":
                self.tratar_opcao_submenu_listar_por_data()
            case "5":
                self.ctrl_tarefa.listar_tarefas_por_importancia()
            case "6":                
                self.main()
            case _:
                print("Opção inválida.\n") 
                return self.tratar_opcao_submenu_listar_tarefas()       


    def tratar_opcao_submenu_listar_por_data(self) -> None:
        self.tela_tarefas.mostrar_submenu_listar_por_data()
        escolha = input()

        match escolha:
            case "1":
                self.ctrl_tarefa.listar_tarefas_por_criacao()
            case "2":
                self.ctrl_tarefa.listar_tarefas_por_finalizacao()           
            case "3":                
                self.main()
            case _:
                print("Opção inválida.\n")
                return self.tratar_opcao_submenu_listar_por_data()      


    def main(self):
        while not self.usuario_logado:
            self.mostrar_menu_inicial()
            escolha = input("Digite sua escolha: ")
            self.tratar_opcao_menu_inicial(escolha)

        
        while self.usuario_logado:
            self.mostrar_menu_tarefas()
            escolha = input("Digite sua escolha: ")
            self.tratar_opcao_menu_tarefas(escolha)