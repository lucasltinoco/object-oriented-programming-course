from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autor = autor
        self.__numeroCapitulo = numeroCapitulo
        self.__tituloCapitulo = tituloCapitulo
        self.__autores = []
        self.__capitulos = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autor(self):
        return self.__autor

    @property
    def numeroCapitulo(self):
        return self.__numeroCapitulo

    @property
    def tituloCapitulo(self):
        return self.__tituloCapitulo

    @property
    def autores(self):
        return self.__autores

    @property
    def capitulos(self):
        return self.__capitulos

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @numeroCapitulo.setter
    def numeroCapitulo(self, numeroCapitulo):
        self.__numeroCapitulo = numeroCapitulo

    @tituloCapitulo.setter
    def tituloCapitulo(self, tituloCapitulo):
        self.__tituloCapitulo = tituloCapitulo

    @autores.setter
    def autores(self, autores):
        self.__autores = autores

    @capitulos.setter
    def capitulos(self, capitulos):
        self.__capitulos = capitulos

    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        self.__autores = [
            a for a in self.__autores if a.codigo != autor.codigo]

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        for cap in self.__capitulos:
            if cap.numeroCapitulo == numeroCapitulo:
                return
        novoCapitulo = Capitulo(numeroCapitulo, tituloCapitulo)
        self.__capitulos.append(novoCapitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        self.__capitulos = [
            c for c in self.__capitulos if c.tituloCapitulo != tituloCapitulo]

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for cap in self.__capitulos:
            if cap.tituloCapitulo == tituloCapitulo:
                return cap
        return None
