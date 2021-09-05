class Livro(object):

    def __init__(self):
        self._categorias = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, edicao):
        self._edicao = edicao

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, editora):
        self._editora = editora

    @property
    def quant_paginas(self):
        return self._quant_paginas

    @quant_paginas.setter
    def quant_paginas(self, quant_paginas):
        self._quant_paginas = quant_paginas

    @property
    def categorias(self):
        return self._categorias

    @categorias.setter
    def categorias(self, categorias):
        self._categorias = categorias