class Livro_Categoria(object):

    @property
    def codigo_livro(self):
        return self._codigo_livro

    @codigo_livro.setter
    def codigo_livro(self, codigo_livro):
        self._codigo_livro = codigo_livro

    @property
    def codigo_categoria(self):
        return self._codigo_categoria

    @codigo_categoria.setter
    def codigo_categoria(self, codigo_categoria):
        self._codigo_categoria = codigo_categoria

    