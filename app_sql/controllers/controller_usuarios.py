from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario
from utils.auxiliar_senhas import gerar_salt, pegar_senha_tratada

class ControllerUsuarios:

    def __init__(self) -> None:
        self.repo_usuario = RepositorioUsuario()      
        

    def cadastrar_usuario(self) -> None:
        
        username = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if username == "" or senha == "":
            print("Campos em branco.\n")
            return self.cadastrar_usuario()
        
        salt = gerar_salt()
        hashed_senha = pegar_senha_tratada(salt, senha)
        if not hashed_senha:
            return self.cadastrar_usuario()
        
        usuario = Usuario(username, hashed_senha, salt)
        
        cadastrado = self.repo_usuario.cadastrar_usuario(usuario)
        if cadastrado:
            print("Cadastrado com sucesso.\n")                        
        else:
            print("Username já existe.\n")
            return self.cadastrar_usuario()           


    def validar_credenciais(self) -> tuple | int:
        
        username = input("\nUsuário: ").strip()
        senha = input("Senha: ").strip()
        
        usuario = self.repo_usuario.selecionar_usuario_por_username(username)

        if not usuario:
            print("Usuário não Cadastrado.\n")
            return 0
        
        senha_tratada = pegar_senha_tratada(usuario.salt, senha)

        if usuario.senha == senha_tratada and usuario.username == username:
            print("Logado com sucesso!\n")
            return (usuario.id_usuario, usuario.username)
        else:
            print("Usuário ou Senha Inválidos.")
            return 0