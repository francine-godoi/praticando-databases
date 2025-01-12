from sqlalchemy.exc import IntegrityError
from models.usuarios import Usuario
from repositories.conexao_db import ConexaoDb


class RepositorioUsuario:    

    def __init__(self) -> None:
        self.conexao = ConexaoDb()
        self.session = self.conexao.criar_session()
        self.criar_tabela_usuario()

    def criar_tabela_usuario(self) -> None:
        Base = self.conexao.pegar_base()
        Base.metadata.create_all(bind=self.conexao.db)

    def cadastrar_usuario(self, usuario: Usuario) -> int:

        try:
            self.session.add(usuario)
            self.session.commit()
            self.session.close()            
            return 1
        except IntegrityError:
            self.session.rollback()
            self.session.close()            
            return 0

    def selecionar_usuario_por_username(self, username: str) -> Usuario:
        
        usuario = (
            self.session.query(Usuario).filter(
                Usuario.username==username)
                .first()
        )
        self.session.close()
        return usuario
