class Usuario:

    def __init__(
        self, username: str, senha: str, salt: str, id_usuario: int = None
    ) -> None:
        self.username = username
        self.senha = senha
        self.salt = salt
        self.id_usuario = id_usuario

    def pegar_info_usuario(self) -> tuple:
        return (self.username, self.senha, self.salt)
    
    def __repr__(self) -> str:
        return f"Sql = Username: {self.username}, Senha: {self.senha}, Salt: {self.salt}"
