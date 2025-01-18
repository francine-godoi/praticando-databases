from config import ORM, SQL, NOSQL

def __importar_repositorio_usuario():
    if ORM:
        from repositories.repositorio_usuario_orm import RepositorioUsuario        
    elif SQL:
        from repositories.repositorio_usuario_sql import RepositorioUsuario
    elif NOSQL:
        from repositories.repositorio_usuario_nosql import RepositorioUsuario
    return RepositorioUsuario

def __importar_repositorio_tarefa():
    if ORM:
        from repositories.repositorio_tarefas_orm import RepositorioTarefa        
    elif SQL:
        from repositories.repositorio_tarefas_sql import RepositorioTarefa 
    elif NOSQL:
        from repositories.repositorio_tarefas_nosql import RepositorioTarefa 
    return RepositorioTarefa


repo_usuario = __importar_repositorio_usuario()
repo_tarefa = __importar_repositorio_tarefa()