from datetime import date
from models.tarefas import Tarefa
from database.conexao_db_nosql import ConexaoDb


class RepositorioTarefa():


    def __init__(self) -> None:
        self.db = ConexaoDb.pegar_db()
        self.collection_tarefa = self.criar_tabela_tarefas()

    def criar_tabela_tarefas(self) -> None:
        collection_tarefa = self.db.tarefas
        return collection_tarefa

    def adicionar_tarefa(self, tarefa: Tarefa) -> int:
        ultimo_registro = self.collection_tarefa.find_one(sort=[('$natural', -1)])
        data = date.today().strftime("%d/%m/%Y")
        info_tarefa = {
            'id_usuario': tarefa.id_usuario,
            'descricao': tarefa.descricao,
            'importancia': tarefa.importancia,
            'status': "A",
            'criado_em': data,
            'finalizado_em': '',
            'id_tarefa': ultimo_registro['id_tarefa'] + 1 if ultimo_registro else 1
            }
        
        resultado = self.collection_tarefa.insert_one(info_tarefa).inserted_id
        print('Usando NoSQL.')              
        return resultado

    def editar_tarefa(self, novos_dados: dict) -> int:        
        filtro = {'id_tarefa': novos_dados['id_tarefa']}
        novos_dados = {'$set': {'descricao': novos_dados['descricao'],
                                'importancia': novos_dados['importancia']}
                      }
        resultado = self.collection_tarefa.update_one(filtro, novos_dados).matched_count
        print('Usando NoSQL.')                      
        return resultado

    def excluir_tarefa(self, tarefa: Tarefa) -> int:
        filtro = {'id_tarefa': tarefa.id_tarefa}
        resultado = self.collection_tarefa.delete_one(filtro).deleted_count
        print('Usando NoSQL.')                      
        return resultado

    def finalizar_tarefa(self, tarefa: Tarefa) -> int:
        filtro = {'id_tarefa': tarefa.id_tarefa}
        data = date.today().strftime("%d/%m/%Y")
        novos_dados = {'$set': {'status': 'F',
                                'finalizado_em': data}
                      }
        resultado = self.collection_tarefa.update_one(filtro, novos_dados).matched_count
        print('Usando NoSQL.')                      
        return resultado

    def selecionar_todas_tarefas(self, id_usuario: int) -> list[Tarefa]:
        resultados = self.collection_tarefa.find({'id_usuario': id_usuario})
        lista_tarefas = self.criar_lista_de_tarefas(resultados)
        return lista_tarefas

    def selecionar_tarefa_por_id(self, id_tarefa: int, id_usuario: int) -> Tarefa:
        resultado = self.collection_tarefa.find_one({'id_usuario': id_usuario, 'id_tarefa': id_tarefa, 'status': 'A'})
        if not resultado:
            return 0

        tarefa = Tarefa(resultado['id_usuario'], resultado['descricao'], resultado['importancia'], resultado['id_tarefa'])
        return tarefa

    def selecionar_tarefas_por_status(self, id_usuario: int, status: str) -> list[Tarefa]:
        resultados = self.collection_tarefa.find({'id_usuario': id_usuario, 'status': status})
        lista_tarefas = self.criar_lista_de_tarefas(resultados)
        return lista_tarefas

    def selecionar_tarefas_por_importancia(self, id_usuario: int, importancia: str) -> list[Tarefa]:     
        resultados = self.collection_tarefa.find({'id_usuario': id_usuario, 'importancia': importancia})
        lista_tarefas = self.criar_lista_de_tarefas(resultados)
        return lista_tarefas

    def selecionar_tarefas_por_data(self, tipo_data: str, id_usuario: int,
                                    data_inicio: str, data_final: str) -> list[Tarefa]:   

        resultados = self.collection_tarefa.find({'id_usuario': id_usuario,
                                                  '$and': [
                                                        {tipo_data:{'$gte': data_inicio}},
                                                        {tipo_data:{'$lte': data_final}}
                                                    ]
                                                })
        lista_tarefas = self.criar_lista_de_tarefas(resultados)
        return lista_tarefas

    def criar_lista_de_tarefas(self, resultados) -> list[Tarefa]:
        lista_tarefas = []
        for resultado in resultados:
            tarefa = Tarefa(
                id_usuario = resultado['id_usuario'],
                id_tarefa = resultado['id_tarefa'],
                descricao = resultado['descricao'],
                importancia = resultado['importancia'],
                status = resultado['status'],
                criado_em = resultado['criado_em'],
                finalizado_em = resultado['finalizado_em'],
            )
            lista_tarefas.append(tarefa)
        return lista_tarefas
