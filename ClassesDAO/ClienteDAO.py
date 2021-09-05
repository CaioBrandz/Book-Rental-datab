import traceback
import psycopg2
from Classes.Cliente import Cliente


# Classe que implementa o padrão DAO para entidade cliente, encapsulando as chamadas SQL DML da entidade pessoa
class ClienteDAO(object):

    # Método utilizado para listar todos os clientes existentes
    def listas_todas(self):
        resultados = []
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, cpf, endereco FROM cliente")
            registros = cursor.fetchall()
            for r in registros:
                c = Cliente()
                c.codigo = r[0]
                c.nome = r[1]
                c.cpf = r[2]
                c.endereco = r[3]
                resultados.append(c)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    # Método utilizado para listar um cliente existente, informando seu código identificado
    def listar(self, codigo):
        c = None
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, cpf, endereco FROM cliente WHERE codigo = " + str(codigo))
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                c = Cliente()
                c.codigo = r[0]
                c.nome = r[1]
                c.cpf = r[2]
                c.endereco = r[3]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    # Método utilizado para inserir um novo cliente
    def inserir(self, codigo, nome, cpf, endereco):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO cliente (codigo, nome, cpf, endereco) VALUES (" + str(codigo) + ", '" + nome + "', '" + str(cpf) + "', '" + endereco + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para atualizar os dados de um cliente existente, filtrando pelo seu código identificador
    def atualizar(self, codigo, nome, cpf, endereco):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("UPDATE cliente SET nome = '" + nome + "', cpf = '" + str(cpf) + "', endereco = '" + endereco + "' WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para remover os dados de um cliente, filtrando pelo seu código identificador
    def remover(self, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cliente WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso