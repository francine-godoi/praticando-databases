# Sistema de Login + Lista de Tarefas

## 📋 Descrição

Segundo mini projeto (via terminal) aplicando conceitos vistos durante minha jornada para aprender Python:

    1. Lógica de programação
    2. POO
    3. MVC
    4. Sql puro (Sqlite)
    5. ORM (SqlAlchemy)
    6. NoSql (MongoDB)

---

## 🧩 Justificativa para o projeto

Para o projeto de fixação dessa etapa me foi recomendado criar um sistema de login usando o SqlAlchemy ORM, mas achei que seria algo muito simples para realmente fixar todos os conceitos que aprendi até o momento, ainda mais que ignora alguns pontos que aprendi antes de chegar ao SqlAlchemy.

Resolvi então a juntar esse projeto com a "lista de tarefas" que é um dos projetos para iniciantes mais recomendados por usar CRUD em várias etapas do seu desenvolvimento.

Outra vantagem de juntar os dois projetos é que agora terei duas tabelas relacionadas para trabalhar com o banco de dados, coisa que não seria possível apenas com o sistema de login.

Para melhor aproveitar e treinar os conhecimentos que adquiri até o momento resolvi criar três versões desse projeto:

1. Usando Sql puro
2. Usando o SqlAlchemy ORM
3. Usando NoSql MongoDB

Dessa forma também posso ver por conta própria a diferença na implementação de cada.

Ao finalizar, criei uma quarta versão 'tudo em um', onde é possível selecionar qual versão vai ser rodada a partir do arquivo de configuração.

---

## 📝 Requisitos do Sistema / Funcionalidades

### Tela inicial

<!-- trunk-ignore(markdownlint/MD033) -->

- <ins>Cadastrar novo usuário:</ins> Usuario, Senha.
  <br>**Restrições:**
  - Campo usuário deve ser único;
  - Senha deve ter pelo menos 8 caracteres, incluindo: letras maiúsculas, minúsculas, números e caracteres especiais;
- <ins>Fazer Login:</ins> Leva o usuário ao sistema de lista de tarefas.
- <ins>Sair do sistema</ins>

### Tela de Lista de Tarefas

**Restrição:** usuário deve estar logado para acessar essa tela

- <ins>Adicionar tarefa:</ins> Descrição, Importância (Alta/Média/Baixa).
  <br>O sistema adiciona automaticamente a data de criação e status "Em andamento";
- <ins>Editar tarefa:</ins> Descrição, Importância. A escolha da tarefa é feita por código.
  <br>**Restrição:** Alteração é permitida apenas para tarefas com status "Em andamento";
- <ins>Excluir tarefa:</ins> A escolha da tarefa é feita por código.
  <br>O sistema dá a opção de listar todas as tarefas "Em andamento" para o usuário consultar o código.
  <br>**Restrição:** Alteração é permitida apenas para tarefas com status "Em andamento";
- <ins>Finalizar tarefa:</ins> A escolha da tarefa é feita por código.
  <br>O sistema dá a opção de listar todas as tarefas "Em andamento" para o usuário consultar o código.
  <br>Atualiza status para "Finalizado" e adiciona a data de finalização.
- <ins>Listar tarefas:</ins> Opções:
  - Todas
  - Em andamento
  - Finalizadas
  - Por data
    - Data criação
    - Data finalização
  - Por importância
    - Alta
    - Média
    - Baixa
- <ins>Sair/Logout:</ins> Finaliza a sessão do usuáiro e volta para a tela inicial

---

## 🔀 Diagrama ER

![diagrama_er_sistema_login_lista_tarefas](https://github.com/user-attachments/assets/930f88e0-8241-4d56-bac0-bded6c9c6ea0)

---

## 📚 Referencias

[Storing and Retrieving Passwords Securely in Python
By Gurpreet Kaur](https://www.askpython.com/python/examples/storing-retrieving-passwords-securely)

[Como Criar Banco de Dados em Python SQLAlchemy por Hashtag Programação](https://www.youtube.com/watch?v=W-g6StRy1zY)

[MongoDB Python Tutorial by Tech With Tim](https://www.youtube.com/playlist?list=PLzMcBGfZo4-nX-NCYorkatzBxjqRlPkKB)

---

## 🛠️ Requerimentos

    `pip install python-dotenv`
    `pip install sqlalchemy`
    `pip install pymongo`

Criar um arquivo .env e armazenar a variável "PEPPER" que será usada no hash das senhas durante o cadastro do usuário.

      PEPPER = "SECRET_KEY"
