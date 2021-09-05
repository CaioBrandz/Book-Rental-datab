class Categoria(object):

    def __init__(self):
        self._livros = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def livros(self):
        return self._livros

    @livros.setter
    def livros(self, livros):
        self._livros = livros