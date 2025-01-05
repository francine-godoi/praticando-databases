# Sistema de Login + Lista de Tarefas

## 📋 Descrição

Segundo mini projeto (via terminal) aplicando conceitos vistos durante minha jornada para aprender Python:

    1. Lógica de programação
    2. POO 
    3. MVC
    4. Sql puro (Sqlite)
    5. SqlAlchemy ORM
    6. NoSql (MongoDB) - futuramente

----

## 🧩 Justificativa para o projeto

Para o projeto de fixação dessa etapa me foi recomendado criar um sistema de login usando o SqlAlchemy ORM, mas achei que seria algo muito simples para realmente fixar todos os conceitos que aprendi até o momento, ainda mais que ignora alguns pontos que aprendi antes de chegar ao SqlAlchemy.

Resolvi então a juntar esse projeto com a "lista de tarefas" que é um dos projetos para iniciantes mais recomendados por usar CRUD em várias etapas do seu desenvolvimento.

Outra vantagem de juntar os dois projetos é que agora terei duas tabelas relacionadas para trabalhar com o banco de dados, coisa que não seria possível apenas com o sistema de login.

Para melhor aproveitar e treinar os conhecimentos que adquiri até o momento resolvi criar duas versões desse projeto:
1. Usando Sql puro
2. Usando o SqlAlchemy ORM
   
Dessa forma também posso ver por conta própria a diferença na implementação dos dois.

Futuramente, considero a possibilidade de criar uma terceira versão do sistema usando NoSql, já que também estudei MongoDB e portanto devo pratica-lo.

----

## 📝 Requisitos do Sistema / Funcionalidades

### Tela inicial

- <ins>Cadastrar novo usuário:</ins> Usuario, Senha.
  <br>**Restrições:** Campo usuário deve ser único; Senha deve ser criptografada;
- <ins>Login</ins>
- <ins>Sair do sistema</ins>


### Tela de Lista de Tarefas
**Restrição:** usuário deve estar logado para acessar essa tela

- <ins>Adicionar tarefa:</ins> Descrição, Importância (Alta/Média/Baixa).
  <br>O sistema adiciona automaticamente a data de criação e status "Em andamento";
  
- <ins>Editar tarefa:</ins> Descrição, Importância.
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
    - data criação 
    - data finalização
  - Por importância
    
- <ins>Sair/Logout:</ins> Finaliza a sessão do usuáiro e volta para a tela inicial

----

## 🔀 Diagrama ER

![diagrama_er_sistema_login_lista_tarefas](https://github.com/user-attachments/assets/930f88e0-8241-4d56-bac0-bded6c9c6ea0)

----

## 📚 Referencias

[Storing and Retrieving Passwords Securely in Python
By Gurpreet Kaur](https://www.askpython.com/python/examples/storing-retrieving-passwords-securely)

----

## 🛠️ Requerimentos

`pip install python-dotenv`