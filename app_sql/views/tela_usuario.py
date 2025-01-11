class TelaUsuario:
    
    def pegar_informacao_usuario(self) -> tuple:
        username = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        return username, senha
    
    def mostrar_mensagem(self, mensagem: str) -> None:
        print(mensagem,'\n')