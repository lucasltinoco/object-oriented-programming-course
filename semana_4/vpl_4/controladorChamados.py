from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def chamados(self):
        return self.__chamados

    @property
    def tipoChamados(self):
        return self.__tipos_chamados

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        total = 0

        for chamado in self.chamados:
            if chamado.tipo.codigo == tipo.codigo:
                total += 1

        return total

    def incluiChamado(self, data: Date, cliente: Cliente,
                      tecnico: Tecnico, titulo: str,
                      descricao: str, prioridade: int,
                      tipo: TipoChamado) -> Chamado:
        if (isinstance(data, Date) and
                isinstance(cliente, Cliente) and
                isinstance(tecnico, Tecnico) and
                isinstance(tipo, TipoChamado)):
            repetido = False

            for chamado in self.chamados:
                if (chamado.data == data and
                        chamado.cliente == cliente and
                        chamado.tecnico == tecnico and
                        chamado.tipo == tipo):
                    repetido = True

            if not repetido:
                chamado = Chamado(data, cliente,
                                  tecnico, titulo,
                                  descricao, prioridade, tipo)
                self.chamados.append(chamado)
                return chamado

    def incluiTipoChamado(self, codigo: int,
                          nome: str, descricao: str) -> TipoChamado:
        repetido = False

        for tipo in self.tipoChamados:
            if tipo.codigo == codigo:
                repetido = True

        if not repetido:
            tipochamado = TipoChamado(codigo, descricao, nome)
            self.tipoChamados.append(tipochamado)
            return tipochamado
