class Autor_Livro(object):

    @property
    def codigo_livro(self):
        return self._codigo_livro

    @codigo_livro.setter
    def codigo_livro(self, codigo_livro):
        self._codigo_livro = codigo_livro

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor