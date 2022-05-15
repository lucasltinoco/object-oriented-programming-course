from abc import abstractmethod
from animal import Animal


class Mamifero(Animal):
    def __init__(self, volume_som: int, tamanho_passo: int):
        Animal.__init__(self, tamanho_passo)
        self.__volume_som = volume_som

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som

    @abstractmethod
    def produzir_som(self):
        pass
