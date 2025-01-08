from models.usuarios import Usuario
from repositories.repositorio_usuario import RepositorioUsuario

from hashlib import sha256
from os import getenv, urandom
import re

from dotenv import load_dotenv

class ControllerUsuarios:

    def __init__(self):
        self.repo_usuario = RepositorioUsuario()      
        

    def cadastrar_usuario(self) -> None:
        
        username = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if username == "" or senha == "":
            print("Campos em branco.\n")
            return self.cadastrar_usuario()
        
        if not self.verificar_senha_forte(senha):
            print("A senha deve conter pelo menos 8 caracteres, incluindo:\n letras maiúsculas, minúsculas, números e caracteres especiais\n")
            return self.cadastrar_usuario()

        salt = self.gerar_salt()
        hashed_senha = self.hash_senha(salt, senha)
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

        senha_tratada = self.hash_senha(salt_salvo, senha)

        if senha_salva == senha_tratada and username_salvo == username:
            print("Logado com sucesso!\n")
            return (id_usuario, username_salvo)
        else:
            print("Usuário ou Senha Inválidos.")
            return 0

    
    def verificar_senha_forte(self, senha) -> bool:        
        """
        ^
        (?=.*[0-9])           // deve conter ao menos um dígito
        (?=.*[a-z])           // deve conter ao menos uma letra minúscula
        (?=.*[A-Z])           // deve conter ao menos uma letra maiúscula
        (?=.*[$&@#])          // deve conter ao menos um caractere especial
        [a-zA-Z0-9$&@#]{8,}   // deve conter ao menos 8 caracteres 
        $
        """
        senha_forte = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$&@#])[a-zA-Z0-9$&@#]{8,}$"       
        return bool(re.match(senha_forte, senha))
    
    
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