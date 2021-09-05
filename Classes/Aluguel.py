class Aluguel(object):

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def codigo_cliente(self):
        return self._codigo_cliente

    @codigo_cliente.setter
    def codigo_cliente(self, codigo_cliente):
        self._codigo_cliente = codigo_cliente

    @property
    def codigo_funcionario(self):
        return self._codigo_funcionario

    @codigo_funcionario.setter
    def codigo_funcionario(self, codigo_funcionario):
        self._codigo_funcionario = codigo_funcionario

    @property
    def tempo_aluguel(self):
        return self._tempo_aluguel

    @tempo_aluguel.setter
    def tempo_aluguel(self, tempo_aluguel):
        self._tempo_aluguel = tempo_aluguel

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def data_aluguel(self):
        return self._data_aluguel

    @data_aluguel.setter
    def data_aluguel(self, data_aluguel):
        self._data_aluguel = data_aluguel