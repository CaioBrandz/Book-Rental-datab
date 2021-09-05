import traceback
import psycopg2
from Classes.Funcionario import Funcionario


class FuncionarioDAO(object):
    # Método utilizado para listar todos os usuarios existentes
    def listas_todas(self):
        resultados = []
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, nome, cpf, endereco, salario FROM funcionario")
            registros = cursor.fetchall()
            for r in registros:
                f = Funcionario()
                f.codigo = r[0]
                f.nome = r[1]
                f.cpf = r[2]
                f.endereco = r[3]
                f.salario = r[4]
                resultados.append(f)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados


    # Método utilizado para inserir uma nova pessoa
    def inserir(self, codigo, nome, cpf, endereco,salario):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO funcionario (codigo, nome, cpf, endereco, salario) VALUES (" + str(codigo) + ", '" + nome + "', '" + str(cpf) + "', '" + endereco + "','" + str(salario) + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para atualizar os dados de uma pessoa existente, filtrando pelo seu código identificador
    def atualizar(self, codigo, nome, cpf, endereco,salario):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("UPDATE funcionario SET nome = '" + nome + "', cpf = '" + str(cpf) + "', endereco = '" + endereco + "', salario = '" + str(salario) + "' WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para remover os dados de uma pessoa existente, filtrando pelo seu código identificador
    def remover(self, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM funcionario WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso