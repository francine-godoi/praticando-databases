from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario

from sqlite3 import IntegrityError
from hashlib import sha256
from os import getenv, urandom

from dotenv import load_dotenv

class ControllerUsuario:

    def __init__(self):
        self.repo_usuario = RepositorioUsuario()

    def cadastrar_usuario(self, username: str, senha: str) -> None:

        salt = self.gerar_salt()
        hashed_senha = self.hash_senha(salt, senha.strip())
        user = Usuario(username.strip(), salt, hashed_senha)
        try:
            self.repo_usuario.cadastrar_usuario(user)
        except IntegrityError:
            print("Username já existe")
        else:
            print("Cadastrado com sucesso.")


    def validar_credenciais(self, nome_usuario: str, senha: str) -> int:
        
        username = nome_usuario.strip()
        info_usuario = self.repo_usuario.selecionar_usuario_por_username(username)

        if not info_usuario:
            print("Usuário não Cadastrado.")
            return 0
        
        id_usuario, username_salvo, senha_salva, salt_salvo = info_usuario

        senha_tratada = self.hash_senha(salt_salvo, senha.strip())

        if senha_salva == senha_tratada and username_salvo == username:
            return id_usuario
        else:
            print("Usuário ou Senha Inválidos")
            return 0

    @staticmethod
    def gerar_salt() -> bytes:
        # valor de salt 128 bits
        salt = urandom(16)        
        return salt    

    @staticmethod
    def gerar_pepper() -> bytes:   
        load_dotenv()
        pepper = getenv("PEPPER")           
        return pepper.encode()

    def hash_senha(self, salt: bytes, senha: str) -> bytes: 
        senha_hash = sha256(salt + senha.encode() + self.gerar_pepper())        
        return salt + senha_hash.digest()