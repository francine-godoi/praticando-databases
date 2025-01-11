from controllers.controller_menus import ControllerMenus

# trunk-ignore(ruff/F401)
from models.tarefas import Tarefa

# trunk-ignore(ruff/F401)
from models.usuarios import Usuario
from utils.conexao_db import Base, db

if __name__ == "__main__":
    Base.metadata.create_all(bind=db)
    ControllerMenus().main()
