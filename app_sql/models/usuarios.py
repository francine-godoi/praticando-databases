class Usuario:

    def __init__(self, username, senha, salt):
        self.username = username        
        self.senha = senha   
        self.salt = salt

    def pegar_info_usuario(self):
        return (self.username, self.senha, self.salt)