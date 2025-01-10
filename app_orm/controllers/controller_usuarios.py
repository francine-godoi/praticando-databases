from models.usuarios import Usuario
from utils.conexao_db import session
from utils.auxiliar_senhas import pegar_senha_tratada, gerar_salt
from sqlalchemy.exc import IntegrityError

class ControllerUsuarios:        

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
        try:
            session.add(user)
            session.commit()
            print("Cadastrado com sucesso.\n") 
        except IntegrityError:
            print("Username já existe.\n")
            return self.cadastrar_usuario()
        except Exception as e:            
            session.rollback()
            print("Não foi possível Cadastrar o usuário. Um erro ocorreu: {e}\n")            


    def validar_credenciais(self) -> tuple | int:
        
        username = input("\nUsuário: ").strip()
        senha = input("Senha: ").strip()
        
        usuario = session.query(Usuario).filter_by(username=username).first()

        if not usuario:
            print("Usuário não Cadastrado.\n")
            return 0

        senha_tratada = pegar_senha_tratada(usuario.salt, senha)

        if usuario.senha == senha_tratada and usuario.username == username:
            print("Logado com sucesso!\n")
            return (usuario.id_usuario, usuario.username)
        else:
            print("Usuário ou Senha Inválidos.")
            return 0