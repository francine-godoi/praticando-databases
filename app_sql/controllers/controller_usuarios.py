from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario
from utils.auxiliar_senhas import gerar_salt, pegar_senha_tratada
from views.tela_usuario import TelaUsuario


class ControllerUsuarios:

    def __init__(self) -> None:
        self.repo_usuario = RepositorioUsuario()
        self.tela_usuario = TelaUsuario()

    def cadastrar_usuario(self) -> None:
        # pega informações para efetuar cadastro
        username, senha = self.tela_usuario.pegar_informacao_usuario()

        if username == "" or senha == "":
            self.tela_usuario.mostrar_mensagem("Campos em branco.")
            return self.cadastrar_usuario()
                        
        if self.existe_username(username):
            self.tela_usuario.mostrar_mensagem("Esse usuário já está cadastrado.")
            return

        # prepara a senha e pega o salt
        salt = gerar_salt()
        hashed_senha = pegar_senha_tratada(salt, senha)
        if not hashed_senha:
            self.tela_usuario.mostrar_mensagem(
            "A senha deve conter pelo menos 8 caracteres, incluindo:\nletras maiúsculas, minúsculas, números e caracteres especiais."        )
            return self.cadastrar_usuario()

        novo_usuario = Usuario(username, hashed_senha, salt)
        # cadastra usuário no banco
        cadastrado = self.repo_usuario.cadastrar_usuario(novo_usuario)
        if cadastrado:
            self.tela_usuario.mostrar_mensagem("Cadastrado com sucesso.")
        else:
            self.tela_usuario.mostrar_mensagem("Username já existe.")
            return self.cadastrar_usuario()

    def validar_credenciais(self) -> Usuario | int:

        username, senha = self.tela_usuario.pegar_informacao_usuario()
        # seleciona o usuário no banco
        usuario = self.repo_usuario.selecionar_usuario_por_username(username)
        if not usuario:
            self.tela_usuario.mostrar_mensagem("Usuário não Cadastrado.")
            return 0

        # prepara a senha para comparação com a senha armazenada no banco
        senha_tratada = pegar_senha_tratada(usuario.salt, senha)
        # valida os dados e retorna o usuário logado se estiver tudo certo
        if usuario.senha == senha_tratada and usuario.username == username:
            self.tela_usuario.mostrar_mensagem("Logado com sucesso!")
            return usuario
        else:
            self.tela_usuario.mostrar_mensagem("Usuário ou Senha Inválidos.")
            return 0

    def existe_username(self, username):
        return self.repo_usuario.selecionar_usuario_por_username(username)