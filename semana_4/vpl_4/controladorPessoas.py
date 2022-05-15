from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        repetido = False

        for cliente in self.clientes:
            if codigo == cliente.codigo:
                repetido = True
                break

        if not repetido:
            c = Cliente(nome, codigo)
            self.__clientes.append(c)
            return c

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        repetido = False

        for tecnico in self.tecnicos:
            if codigo == tecnico.codigo:
                repetido = True
                break

        if not repetido:
            t = Tecnico(nome, codigo)
            self.__tecnicos.append(t)
            return t
