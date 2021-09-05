import traceback
import psycopg2
from Classes.Livro import Livro
from Classes.Categoria import Categoria
from Classes.Autor_livro import Autor_Livro


class LivroDAO(object):

    # Listar todos os livros
    def listar_todos(self):
        resultados = []

        try:
            connection = psycopg2.connect(user = 'postgres', password = '1234', host = 'localhost', port = '5432', database = 'livros')
            cursor = connection.cursor()
            cursor.execute("SELECT codigo,titulo,ano,edicao,editora,quant_paginas FROM livro")
            registros =  cursor.fetchall()
            for r in registros:
                l = Livro()
                l.codigo = r[0]
                l.titulo = r[1]
                l.ano = r[2]
                l.edicao = r[3]
                l.editora = r[4]
                l.quant_paginas = r[5]
                resultados.append(l)

        except(Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultados

    def listar_um_livro(self, _codigo):
        l = None # Inicialização da variável a ser retornada

        try:
            # Estabelecer Conxeão ao BD
            connection = psycopg2.connect(user = 'postgres', password = '1234', host = 'localhost', port = '5432', database = 'livros')
            cursor = connection.cursor()
            # Executar comando
            cursor.execute("SELECT codigo,titulo,ano,edicao,editora,quant_paginas FROM livro WHERE codigo = " + str(_codigo))
            r = cursor.fetchone() # Pegar o resultado

            if cursor.rowcount == 1:
                l = Livro()
                l.codigo = r[0]
                l.titulo = r[1]
                l.ano = r[2]
                l.edicao = r[3]
                l.editora = r[4]
                l.quant_paginas = r[5]

        except(Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        
        return l

    def listar_categorias(self, codigo):
        l = None
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursorLivro = connection.cursor()
            cursorLivro.execute("SELECT codigo, titulo, ano, edicao, editora, quant_paginas FROM livro WHERE codigo = %s" % codigo)
            r = cursorLivro.fetchone();
            if cursorLivro.rowcount == 1:
                l = Livro()
                l.codigo = r[0]
                l.titulo = r[1]
                l.ano = r[2]
                l.edicao = r[3]
                l.editora = r[4]
                l.quant_paginas = r[5]
                cursorCategoria = connection.cursor()
                cursorCategoria.execute("SELECT c.codigo, c.descricao FROM livro_categoria AS lc, categoria AS c WHERE lc.codigo_categoria = c.codigo AND lc.codigo_livro = %s" % r[0])
                categorias = cursorCategoria.fetchall()
                for categoria in categorias:
                    c = Categoria()
                    c.codigo = categoria[0]
                    c.descricao = categoria[1]
                    l.categorias.append(c)
                cursorCategoria.close()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursorLivro.close()
                connection.close()
        return l

    def inserir(self, codigo, titulo, ano, edicao ,editora,quant_paginas):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO livro (codigo, titulo, ano, edicao, editora, quant_paginas) VALUES (" + str(codigo) + ", '" + titulo + "', '" + str(ano) + "', '" + str(edicao) + "','" + editora + "','" + str(quant_paginas) + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def inserir_autor(self, codigo_livro,autor):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO autor_livro (codigo_livro, autor) VALUES (" + str(codigo_livro) + ", '" + autor + "')")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def atualizar(self, codigo, titulo, ano, edicao ,editora,quant_paginas):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("UPDATE livro SET titulo = '" + titulo + "', ano = '" + str(
                ano) + "', edicao = '" + str(edicao) + "', editora = '" + editora + "', quant_paginas = '" + str(quant_paginas) + "' WHERE codigo = " + str(
                codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover(self, codigo):
        sucesso = False
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM livro WHERE codigo = " + str(codigo) + "")
            connection.commit()
            sucesso = (cursor.rowcount == 1)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso