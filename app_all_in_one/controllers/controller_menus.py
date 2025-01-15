from controllers.controller_tarefas import ControllerTarefas
from controllers.controller_usuarios import ControllerUsuarios
from views.tela_inicial import TelaInicial
from views.tela_tarefas import TelaTarefas
from utils.importador_classe_dinamico import model_usuario as Usuario


class ControllerMenus:

    def __init__(self) -> None:
        self.tela_inicial = TelaInicial()
        self.tela_tarefas = TelaTarefas()
        self.ctrl_usuario = ControllerUsuarios()
        self.ctrl_tarefa = None
        self.usuario_logado = None

    def mostrar_menu_inicial(self) -> None:
        # mostra menu inicial para cadastrar novo usuário ou fazer login no sistema
        self.tela_inicial.mostrar_menu_inicial()

    def mostrar_menu_tarefas(self) -> None:
        # após estar logado o usuário tem acesso ao sistema de tarefas
        self.tela_tarefas.mostrar_menu_tarefas(self.usuario_logado.username)

    def tratar_opcao_menu_inicial(self, escolha: str) -> None:
        # usuário é cadastrado ou faz login
        match escolha:
            case "1":
                self.ctrl_usuario.cadastrar_usuario()
            case "2":
                # valida os dados de login do usuário
                usuario_logado: Usuario = self.ctrl_usuario.validar_credenciais()
                if usuario_logado:
                    self.usuario_logado = usuario_logado
                    # se usuário está logado ele é vinculado as tarefas do sistema de tarefas
                    self.ctrl_tarefa = ControllerTarefas(
                        usuario_logado.id_usuario
                    )
            case "3":
                print("Tchau!!")
                exit()
            case _:
                print("Opção inválida.\n")

    def tratar_opcao_menu_tarefas(self, escolha: str) -> None:
        # menu de gerenciamento das tarefas, só é usado quando o usuário está logado
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
                # há varias opções de listagem, serão exibidas nesse submenu
                self.tratar_opcao_submenu_listar_tarefas()
            case "6":
                self.usuario_logado = False
                self.main()
            case _:
                print("Opção inválida.\n")

    def tratar_opcao_submenu_listar_tarefas(self) -> None:
        # usuário escolhe como ele quer que as tarefas sejam listadas
        self.tela_tarefas.mostrar_submenu_listar_tarefas()
        escolha = input()

        match escolha:
            case "1":
                self.ctrl_tarefa.listar_todas_tarefas()
            case "2":
                self.ctrl_tarefa.listar_tarefas_por_status("A")
            case "3":
                self.ctrl_tarefa.listar_tarefas_por_status("F")
            case "4":
                # existe 2 opções de datas para serem escolhidas, são tratadas nesse submenu
                self.tratar_opcao_submenu_listar_por_data()
            case "5":
                self.ctrl_tarefa.listar_tarefas_por_importancia()
            case "6":
                self.main()
            case _:
                print("Opção inválida.\n")
                return self.tratar_opcao_submenu_listar_tarefas()

    def tratar_opcao_submenu_listar_por_data(self) -> None:
        # usuário escolhe qual tipo de data ele quer filtrar as tarefas
        self.tela_tarefas.mostrar_submenu_listar_por_data()
        escolha = input()

        match escolha:
            case "1":
                self.ctrl_tarefa.listar_tarefas_por_data("criado_em")
            case "2":
                self.ctrl_tarefa.listar_tarefas_por_data("finalizado_em")
            case "3":
                self.main()
            case _:
                print("Opção inválida.\n")
                return self.tratar_opcao_submenu_listar_por_data()

    def main(self):
        # usuário não logado vê a tela inicial
        while not self.usuario_logado:
            self.mostrar_menu_inicial()
            escolha = input("Digite sua escolha: ")
            self.tratar_opcao_menu_inicial(escolha)

        # usuário logado tem acesso ao sistema de tarefas
        while self.usuario_logado:
            self.mostrar_menu_tarefas()
            escolha = input("Digite sua escolha: ")
            self.tratar_opcao_menu_tarefas(escolha)
