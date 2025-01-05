class Usuario:

    def __init__(self, username, salt, senha):
        self.username = username
        self.salt = salt
        self.senha = senha   

    def pegar_info_usuario(self):
        return (self.username, self.senha, self.salt)

    

    