from repositories.repositorio_usuario import RepositorioUsuario
from hashlib import sha256
from os import getenv
from dotenv import load_dotenv

class ControllerUsuario:

    def __init__(self):
        self.repo_usuario = RepositorioUsuario()

    def validar_credenciais(self, username, senha): 

        load_dotenv()
        PEPPER = getenv("PEPPER")        
        
        info_usuario = self.repo_usuario.selecionar_usuario_por_username(username)
        
        if info_usuario is None:
            print("Usuário não Cadastrado.")
            return False
        
        username_salvo = info_usuario[1]
        hashed_senha = info_usuario[2]
        salt = info_usuario[3]

        senha_tratada = salt + (sha256(salt + senha.encode() + PEPPER.encode())).digest()

        if hashed_senha == senha_tratada and username_salvo == username:
            return info_usuario[0] # retorna o id_usuario
        else:
            print("Usuário ou Senha Inválidas")
            return False
        