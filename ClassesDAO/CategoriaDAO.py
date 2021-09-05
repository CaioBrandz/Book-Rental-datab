import traceback
import psycopg2
from Classes.Categoria import Categoria
from Classes.Livro import Livro


# Classe que implementa o padrão DAO para entidade categoria, encapsulando as chamadas SQL DML da entidade categoria
class CategoriaDAO(object):

    # Método utilizado para listar uma categoria existente, informando seu identificador
    def listar_uma_categoria(self, codigo):
        c = None
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursor = connection.cursor()
            cursor.execute("SELECT codigo, descricao FROM categoria WHERE codigo = %s" % codigo)
            r = cursor.fetchone();
            if cursor.rowcount == 1:
                c = Categoria()
                c.codigo = r[0]
                c.descricao = r[1]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    def listar_livros_uma_categoria(self, codigo):
        c = None
        try:
            connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="livros")
            cursorCategoria = connection.cursor()
            cursorCategoria.execute("SELECT codigo, descricao from categoria WHERE codigo = %s" % codigo)
            r = cursorCategoria.fetchone();
            if cursorCategoria.rowcount == 1:
                c = Categoria()
                c.codigo = r[0]
                c.descricao = r[1]
                cursorLivro = connection.cursor()
                cursorLivro.execute("select l.codigo,l.titulo,l.ano, l.edicao, l.editora,l.quant_paginas from livro as l,categoria as c,livro_categoria as lc where c.codigo= lc.codigo_categoria and l.codigo = lc.codigo_livro and c.codigo = %s" % r[0])
                livros = cursorLivro.fetchall()
                for livro in livros:
                    l = Livro()
                    l.codigo = livro[0]
                    l.titulo = livro[1]
                    l.ano = livro[2]
                    l.edicao = livro[3]
                    l.editora = livro[4]
                    l.quant_paginas = livro[5]
                    c.livros.append(l)
                    cursorLivro.close()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursorCategoria.close()
                connection.close()
        return c