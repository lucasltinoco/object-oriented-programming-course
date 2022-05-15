from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        self.__livros = [
            l for l in self.__livros if l.codigo != livro.codigo]

    @property
    def livros(self):
        return self.__livros
