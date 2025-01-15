from config import ORM, SQL

def __importar_model_usuario():
    if ORM:
        from models.usuarios_orm import Usuario        
    elif SQL:
        from models.usuarios_sql import Usuario
    return Usuario

def __importar_repositorio_usuario():
    if ORM:
        from repositories.repositorio_usuario_orm import RepositorioUsuario        
    elif SQL:
        from repositories.repositorio_usuario_sql import RepositorioUsuario
    return RepositorioUsuario

def __importar_model_tarefa():
    if ORM:
        from models.tarefas_orm import Tarefa        
    elif SQL:
        from models.tarefas_sql import Tarefa
    return Tarefa

def __importar_repositorio_tarefa():
    if ORM:
        from repositories.repositorio_tarefas_orm import RepositorioTarefa        
    elif SQL:
        from repositories.repositorio_tarefas_sql import RepositorioTarefa  
    return RepositorioTarefa


model_usuario = __importar_model_usuario()
repo_usuario = __importar_repositorio_usuario()

model_tarefa = __importar_model_tarefa()
repo_tarefa = __importar_repositorio_tarefa()