from hashlib import sha256
from dotenv import load_dotenv
from os import urandom, getenv

class Usuario:

    load_dotenv()
    PEPPER = getenv("PEPPER")

    def __init__(self, username, senha):
        self.username = username
        self.salt = self.gerar_salt()
        self.senha = self.hash_senha(senha)     


    @staticmethod
    def gerar_salt() -> bytes:
        # valor de salt 128 bits
        salt = urandom(16)        
        return salt
    

    @classmethod
    def gerar_pepper(cls) -> bytes:             
        return cls.PEPPER.encode()


    def hash_senha(self, senha) -> bytes:
        senha_hash = sha256(self.salt + senha.encode() + self.gerar_pepper())        
        return self.salt + senha_hash.digest()
    

    def pegar_info_usuario(self):
        return (self.username, self.senha, self.salt)

    

    