class Usuario:

    def __init__(self, username: str, senha: str, salt: str):
        self.username = username        
        self.senha = senha   
        self.salt = salt

    def pegar_info_usuario(self) -> tuple:
        return (self.username, self.senha, self.salt)