from repositories.repositorio_usuario import RepositorioUsuario
from controllers.controller_usuarios import ControllerUsuario

# rep = RepositorioUsuario()
# idu = rep.selecionar_usuario_por_username("aa")
# print(idu)

c = ControllerUsuario().validar_credenciais("bb", "bb")
if c:
    print("Usuário Logado com sucesso.")
else:
    print("Não foi possível fazer o login.")