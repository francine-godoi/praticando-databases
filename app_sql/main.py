from controllers.controller_usuarios import ControllerUsuario

# TESTES

ctrl = ControllerUsuario()
ctrl.cadastrar_usuario("username3", "senha_forte3")

user = input("user ")
senha = input("senha ")
c = ControllerUsuario().validar_credenciais(user, senha)
if c:
    print("Usuário Logado com sucesso.")
else:
    print("Não foi possível fazer o login.")