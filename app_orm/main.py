from controllers.controller_menus import ControllerMenus
from models.usuarios import Usuario
from models.tarefas import Tarefa
from utils.conexao_db import Base, db

if __name__ == "__main__":
    Base.metadata.create_all(bind=db)
    ControllerMenus().main()