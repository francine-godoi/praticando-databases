from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario
from views.tela_usuario import TelaUsuario
from utils.auxiliar_senhas import gerar_salt, pegar_senha_tratada


class ControllerUsuarios:

    def __init__(self) -> None:
        self.repo_usuario = RepositorioUsuario()
        self.tela_usuario = TelaUsuario()

    def cadastrar_usuario(self) -> None:

        username, senha = self.tela_usuario.pegar_informacao_usuario()

        if username == "" or senha == "":
            self.tela_usuario.mostrar_mensagem("Campos em branco.")
            return self.cadastrar_usuario()

        salt = gerar_salt()
        hashed_senha = pegar_senha_tratada(salt, senha)
        if not hashed_senha:
            return self.cadastrar_usuario()

        usuario = Usuario(username, hashed_senha, salt)

        cadastrado = self.repo_usuario.cadastrar_usuario(usuario)
        if cadastrado:
            self.tela_usuario.mostrar_mensagem("Cadastrado com sucesso.")
        else:
            self.tela_usuario.mostrar_mensagem("Username já existe.")
            return self.cadastrar_usuario()

    def validar_credenciais(self) -> tuple | int:

        username, senha = self.tela_usuario.pegar_informacao_usuario()

        usuario = self.repo_usuario.selecionar_usuario_por_username(username)

        if not usuario:
            self.tela_usuario.mostrar_mensagem("Usuário não Cadastrado.")
            return 0

        senha_tratada = pegar_senha_tratada(usuario.salt, senha)

        if usuario.senha == senha_tratada and usuario.username == username:
            self.tela_usuario.mostrar_mensagem("Logado com sucesso!")
            return (usuario.id_usuario, usuario.username)
        else:
            self.tela_usuario.mostrar_mensagem("Usuário ou Senha Inválidos.")
            return 0
