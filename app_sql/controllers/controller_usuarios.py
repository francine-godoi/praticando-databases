from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario
from utils.auxiliar_senhas import pegar_senha_tratada, gerar_salt

class ControllerUsuarios:

    def __init__(self):
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
        
        user = Usuario(username, hashed_senha, salt)
        
        cadastrado = self.repo_usuario.cadastrar_usuario(user)
        if cadastrado:
            print("Cadastrado com sucesso.\n")                        
        else:
            print("Username já existe.\n")
            return self.cadastrar_usuario()           


    def validar_credenciais(self) -> tuple | int:
        
        username = input("\nUsuário: ").strip()
        senha = input("Senha: ").strip()
        
        info_usuario = self.repo_usuario.selecionar_usuario_por_username(username)

        if not info_usuario:
            print("Usuário não Cadastrado.\n")
            return 0
        
        id_usuario, username_salvo, senha_salva, salt_salvo = info_usuario

        senha_tratada = pegar_senha_tratada(salt_salvo, senha)

        if senha_salva == senha_tratada and username_salvo == username:
            print("Logado com sucesso!\n")
            return (id_usuario, username_salvo)
        else:
            print("Usuário ou Senha Inválidos.")
            return 0