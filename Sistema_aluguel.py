from ClassesDAO.ClienteDAO import ClienteDAO
from ClassesDAO.FuncionarioDAO import FuncionarioDAO
from ClassesDAO.LivroDAO import LivroDAO
from ClassesDAO.CategoriaDAO import CategoriaDAO

# Classe que implementa as telas da aplicação e também é classe que inicia a aplicação
class AluguelPython(object):

    # Menu principal da aplicação
    def menu_principal(self):
        print("==========================================")
        print("Sistema de Alugueis Python")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("0\t\tSair da Aplicação")
        print("1\t\tOperações de Clientes")
        print("2\t\tOperações de Funcionario")
        print("3\t\tOperações de Livro")
        print("4\t\tOperações de Categoria")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-4]: "))
        if opcao == 0:
            return
        if opcao == 1:
            self.menu_clientes()
            return
        if opcao == 2:
            self.menu_funcionarios()
            return
        if opcao == 3:
            self.menu_livros()
            return
        if opcao == 4:
            self.menu_categorias()
            return
        self.menu_principal()

    # Menu que exibe as opções para o cliente
    def menu_clientes(self):
        print("==========================================")
        print("Operações do cliente")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("0\t\tVoltar ao Menu Principal")
        print("1\t\tListar Todos os Clientes Existentes")
        print("2\t\tListar um Cliente Existente")
        print("3\t\tInserir um Novo Cliente")
        print("4\t\tAtualizar um Cliente Existente")
        print("5\t\tRemover um Cliente Existente")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-5]: "))
        if opcao == 0:
            self.menu_principal()
            return
        if opcao == 1:
            self.menu_listar_todos_clientes()
            return
        if opcao == 2:
            self.menu_listar_um_cliente()
            return
        if opcao == 3:
            self.menu_inserir_um_cliente()
            return
        if opcao == 4:
            self.menu_atualizar_um_cliente()
            return
        if opcao == 5:
            self.menu_remover_um_cliente()
            return
        self.menu_clientes()

    # Menu que exibe a ação para listar todos os clientes cadastradas
    def menu_listar_todos_clientes(self):
        print("==========================================")
        print("Listar Todos os Clientes Existentes")
        print("==========================================")
        clienteDAO = ClienteDAO()
        clientes = clienteDAO.listas_todas()
        for c in clientes:
            print("*** Código: " + str(c.codigo) + " - Nome: " + c.nome + " - CPF: " + str(c.cpf) + " - Endereco: " + c.endereco + " ***")
        print("*** " + str(len(clientes)) + " clientes(s) encontrada(s) ***")
        self.menu_clientes()

    # Menu que exibe a ação para listar um cliente existente
    def menu_listar_um_cliente(self):
        print("==========================================")
        print("Listar um Cliente Existente")
        print("==========================================")
        codigo = int(input("Digite o código do cliente: "))
        clienteDAO = ClienteDAO()
        cliente = clienteDAO.listar(codigo)
        if cliente is not None:
            print("*** Código: " + str(cliente.codigo) + " - Nome: " + cliente.nome + " - CPF: " + str(cliente.cpf) + " - Endereco: " + cliente.endereco + " ***")
        else:
            print("*** Não foi possível localizar este funcionario ***")
        self.menu_clientes()

    # Menu que exibe a ação para inserir um novo cliente
    def menu_inserir_um_cliente(self):
        print("==========================================")
        print("Inserir um Novo Cliente")
        print("==========================================")
        codigo = int(input("Digite o código do novo cliente: "))
        nome = input("Digite o nome do novo cliente: ")
        cpf = input("Digite o cpf do novo cliente: ")
        endereco = input("Digite o endereco do novo cliente: ")
        clienteDAO = ClienteDAO()
        sucesso = clienteDAO.inserir(codigo, nome, cpf, endereco)
        if sucesso == True:
            print("*** Cliente inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este cliente ***")
        self.menu_clientes()

    # Menu que exibe a ação para atualizar os dados de um cliente
    def menu_atualizar_um_cliente(self):
        print("==========================================")
        print("Atualizar um Cliente Existente")
        print("==========================================")
        codigo = int(input("Digite o código do cliente: "))
        nome = input("Digite o novo nome do cliente: ")
        cpf = input("Digite o novo cpf do cliente: ")
        endereco = input("Digite o novo endereco do cliente: ")
        clienteDAO = ClienteDAO()
        sucesso = clienteDAO.atualizar(codigo, nome, cpf, endereco)
        if sucesso == True:
            print("*** Cliente atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este cliente ***")
        self.menu_clientes()

    # Menu que exibe a ação para remover um cliente
    def menu_remover_um_cliente(self):
        print("==========================================")
        print("Remover um Cliente Existente")
        print("==========================================")
        codigo = int(input("Digite o código do cliente: "))
        clienteDAO = ClienteDAO()
        sucesso = clienteDAO.remover(codigo)
        if sucesso == True:
            print("*** Cliente removido com sucesso ***")
        else:
            print("*** Não foi possível remover este cliente ***")
        self.menu_clientes()

        #FUNCIONARIO------------------------------------------------------------------------

    def menu_funcionarios(self):
        print("==========================================")
        print("Operações do Funcionario")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("0\t\tVoltar ao Menu Principal")
        print("1\t\tListar Todos os Funcionarios existentes")
        print("2\t\tInserir um Funcionarios")
        print("3\t\tAtualizar um Funcionarios")
        print("4\t\tRemover um Funcionarios")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-4]: "))
        if opcao == 0:
            self.menu_principal()
            return
        if opcao == 1:
            self.menu_listar_todos_funcionarios()
            return
        if opcao == 2:
            self.menu_inserir_um_funcionario()
            return
        if opcao == 3:
            self.menu_atualizar_um_funcionario()
            return
        if opcao == 4:
            self.menu_remover_um_funcionario()
            return
        self.menu_funcionarios()

# Menu que exibe a ação para listar todos os funcionarios
    def menu_listar_todos_funcionarios(self):
        print("==========================================")
        print("Listar Todos os Funcionarios Existentes")
        print("==========================================")
        funcionarioDAO = FuncionarioDAO()
        funcionarios = funcionarioDAO.listas_todas()
        for f in funcionarios:
            print("*** Código: " + str(f.codigo) + " - Nome: " + f.nome + " - CPF: " + str(f.cpf) + " - Endereco: " + f.endereco + " - Salario: " + str(f.salario) +"***")
        print("*** " + str(len(funcionarios)) + " pessoa(s) encontrada(s) ***")
        self.menu_funcionarios()

# Menu que exibe a ação para inserir um novo funcionario
    def menu_inserir_um_funcionario(self):
        print("==========================================")
        print("Inserir um novo funcionario")
        print("==========================================")
        codigo = int(input("Digite o código do novo funcionario: "))
        nome = input("Digite o nome do novo funcionario: ")
        cpf = input("Digite o cpf do novo funcionario: ")
        endereco = input("Digite o endereco do novo funcionario: ")
        salario = input("Digite o salario do novo funcionario: ")
        funcionarioDAO = FuncionarioDAO()
        sucesso = funcionarioDAO.inserir(codigo, nome, cpf, endereco,salario)
        if sucesso == True:
            print("*** Funcionario inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir esta pessoa ***")
        self.menu_funcionarios()

# Menu que exibe a ação para atualizar os dados de um funcionario
    def menu_atualizar_um_funcionario(self):
        print("==========================================")
        print("Atualizar um Funcionario existente")
        print("==========================================")
        codigo = int(input("Digite o código do Funcionario: "))
        nome = input("Digite o novo nome do Funcionario: ")
        cpf = input("Digite o novo cpf do Funcionario: ")
        endereco = input("Digite o novo endereco do Funcionario: ")
        salario = input("Digite o novo salario do Funcionario: ")
        funcionarioDAO = FuncionarioDAO()
        sucesso = funcionarioDAO.atualizar(codigo, nome, cpf, endereco,salario)
        if sucesso == True:
            print("*** Funcionario atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este funcionario ***")
        self.menu_funcionarios()

    # Menu que exibe a ação para remover um funcionario existente
    def menu_remover_um_funcionario(self):
        print("==========================================")
        print("Remover um Funcionario Existente")
        print("==========================================")
        codigo = int(input("Digite o código da pessoa: "))
        funcionarioDAO = FuncionarioDAO()
        sucesso = funcionarioDAO.remover(codigo)
        if sucesso == True:
            print("*** Funcionario removido com sucesso ***")
        else:
            print("*** Não foi possível remover este funcionario ***")
        self.menu_funcionarios()

        #LIVROS -------------------------------------------------------------------------------------

    def menu_livros(self):
        print("==========================================")
        print("Operações de livro")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("0\t\tVoltar ao Menu Principal")
        print("1\t\tListar Todos os Livros")
        print("2\t\tListar Livro Existente")
        print("3\t\tListar as Categorias de um Livro existente")
        print("4\t\tInserir um novo livro")
        print("5\t\tInserir um autor para um livro")
        print("6\t\tAtualizar um livro existente")
        print("7\t\tRemover um livro existente")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-7]: "))
        if opcao == 0:
            self.menu_principal()
            return
        if opcao == 1:
            self.menu_listar_todos_livros()
            return
        if opcao == 2:
            self.menu_listar_um_livro()
            return
        if opcao == 3:
            self.menu_listar_categorias_um_livro()
            return
        if opcao == 4:
            self.menu_inserir_um_livro()
            return
        if opcao == 5:
            self.menu_inserir_um_autor()
            return
        if opcao == 6:
            self.menu_atualizar_um_livro()
            return
        if opcao == 7:
            self.menu_remover_um_livro()
            return
        self.menu_livros()

    def menu_listar_todos_livros(self):
        print("==========================================")
        print("Listar Todos os Livros Existentes")
        print("==========================================")
        livroDAO = LivroDAO()
        livros = livroDAO.listar_todos()
        for l in livros:
            print("*** Código: " + str(l.codigo) + " - Titulo: " + l.titulo + " - Ano: " + str(l.ano) + " - Edicao: " + str(l.edicao) + " - Editora: " + l.editora + " - Quantidade de paginas: " + str(l.quant_paginas) + "***")
        print("*** " + str(len(livros)) + " livro(s) encontrado(s) ***")
        self.menu_livros()

    def menu_listar_um_livro(self):
        print("==========================================")
        print("Listar um Livro Existente")
        print("==========================================")
        codigo = int(input("Digite o código do livro: "))
        livroDAO = LivroDAO()
        livro = livroDAO.listar_um_livro(codigo)
        if livro is not None:
            print("*** Código: " + str(livro.codigo) + " - Titulo: " + livro.titulo + " - Ano: " + str(livro.ano) + " - Edicao: " + str(livro.edicao) + " - Editora: " + livro.editora + " - Quantidade de paginas: " + str(livro.quant_paginas) + "***")
        else:
            print("*** Não foi possível localizar este livro ***")
        self.menu_livros()

    def menu_listar_categorias_um_livro(self):
        print("==========================================")
        print("Listar as Categorias de um Livro")
        print("==========================================")
        livroId = int(input('Entre o codigo do livro: '))
        print("==========================================")
        livroDAO = LivroDAO()
        livro = livroDAO.listar_categorias(livroId)
        if livro is not None:
            print("Dados do Livro de Codigo = %s" % livroId)
            print("Livro - Codigo: %s - Titulo: %s - Ano: %s - Edicao: %s - Editora: %s - Paginas: %s - Qtd. Categorias: %s" % (
                livro.codigo, livro.titulo, livro.ano, livro.edicao, livro.editora, livro.quant_paginas,
                len(livro.categorias)))
            print("Categorias do Livro: %s" % livro.titulo)
            for c in livro.categorias:
                print("Codigo: %s - Descricao: %s" % (c.codigo, c.descricao))
        else:
            print("*** Não foi possível localizar este livro ***")
        self.menu_livros()

    def menu_inserir_um_livro(self):
        print("==========================================")
        print("Inserir um novo livro")
        print("==========================================")
        codigo = int(input("Digite o código do novo livro: "))
        titulo = input("Digite o titulo do novo livro: ")
        ano = int(input("Digite o ano do novo livro: "))
        edicao = int(input("Digite a edicao do novo livro: "))
        editora = input("Digite a editora do novo livro: ")
        quant_paginas = int(input("Digite a quantidade de paginas do novo livro: "))
        livroDAO = LivroDAO()
        sucesso = livroDAO.inserir(codigo, titulo, ano,edicao,editora,quant_paginas)
        if sucesso == True:
            print("*** Livro inserido com sucesso ***")
        else:
            print("*** Não foi possível inserir este livro ***")
        self.menu_livros()

    def menu_inserir_um_autor(self):
        print("==========================================")
        print("Inserir um autor para um livro")
        print("==========================================")
        codigo = int(input("Digite o código do livro: "))
        autor = input("Digite o nome do autor: ")
        livroDAO = LivroDAO()
        sucesso = livroDAO.inserir_autor(codigo, autor)
        if sucesso == True:
            print("*** Autor inserido com sucesso para o livro ***")
        else:
            print("*** Não foi possível inserir o autor para este livro ***")
        self.menu_livros()

    def menu_atualizar_um_livro(self):
        print("==========================================")
        print("Atualizar um Livro existente")
        print("==========================================")
        codigo = int(input("Digite o código do Livro a atualizar: "))
        titulo = input("Digite o novo titulo do Livro: ")
        ano = int(input("Digite o novo ano do Livro: "))
        edicao = int(input("Digite o novo numero de edicao do Livro: "))
        editora = input("Digite a nova editora do Livro: ")
        quant_paginas = int(input("Digite a nova quantidade de paginas do Livro: "))
        livroDAO = LivroDAO()
        sucesso = livroDAO.atualizar(codigo, titulo,ano,edicao,editora,quant_paginas)
        if sucesso == True:
            print("*** Livro atualizado com sucesso ***")
        else:
            print("*** Não foi possível atualizar este livro ***")
        self.menu_livros()

    def menu_remover_um_livro(self):
        print("==========================================")
        print("Remover um Livro Existente")
        print("==========================================")
        print("DICA: Você nao conseguirá remover um livro se este estiver em algum aluguel")
        codigo = int(input("Digite o código do livro a ser removido: "))
        livroDAO = LivroDAO()
        sucesso = livroDAO.remover(codigo)
        if sucesso == True:
            print("*** Livro removido com sucesso ***")
        else:
            print("*** Não foi possível remover este livro ***")
        self.menu_livros()

    # CATEGORIA -------------------------------------------------------------------------------------

    def menu_categorias(self):
        print("==========================================")
        print("Operações de categorias")
        print("==========================================")
        print("Opção\tDescrição")
        print("------------------------------------------")
        print("0\t\tVoltar ao Menu Principal")
        print("1\t\tListar uma categoria existente")
        print("2\t\tListar todos os livros de uma Categoria")
        print("------------------------------------------")
        opcao = int(input("Digite uma opção [0-2]: "))
        if opcao == 0:
            self.menu_principal()
            return
        if opcao == 1:
            self.menu_listar_uma_categoria()
            return
        if opcao == 2:
            self.menu_listar_livros_de_uma_categoria()
            return
        self.menu_categorias()

    def menu_listar_uma_categoria(self):
        print("==========================================")
        print("Listar uma Categoria Existente")
        print("==========================================")
        codigo = int(input("Digite o código da categoria: "))
        categoriaDAO = CategoriaDAO()
        categoria = categoriaDAO.listar_uma_categoria(codigo)
        if categoria is not None:
            print("*** Código: " + str(categoria.codigo) + " - Descricao: " + categoria.descricao + " ***")
        else:
            print("*** Não foi possível localizar esta categoria ***")
        self.menu_categorias()

    def menu_listar_livros_de_uma_categoria(self):
        print("==========================================")
        print("Listar todos os livros de uma Categoria")
        print("==========================================")
        codigo = int(input('Digite o codigo da categoria: '))
        print("==========================================")
        categoriaDAO = CategoriaDAO()
        categoria = categoriaDAO.listar_livros_uma_categoria(codigo)

        if categoria is not None:
            print("Categoria selecionada: Codigo: %s - Descricao: %s - Quantidade de Livros: %s" % (categoria.codigo, categoria.descricao, len(categoria.livros)))
            for l in categoria.livros:
                print("Codigo do livro: %s - Titulo: %s - Ano: %s - Edicao: %s - Editora: %s - Paginas: %s" % (l.codigo, l.titulo,l.ano,l.edicao,l.editora, l.quant_paginas))
        else:
            print("*** Não foi possível localizar esta categoria ***")
        self.menu_categorias()


# Código principal que inicializa a aplicação
if __name__ == "__main__":
    aluguel_python = AluguelPython()
    aluguel_python.menu_principal()