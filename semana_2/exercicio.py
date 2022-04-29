class MinhaLista():

    def __init__(self, lista):
        self.tupla = tuple(lista)

    def append(self, variavelAdicionada):
        tempTupla = self.tupla
        self.tupla = (*tempTupla, variavelAdicionada)

    def remove(self, variavelRemovida):
        posicaoRemovida = -1
        for index, valor in enumerate(reversed(self.tupla)):
            if (valor == variavelRemovida):
                posicaoRemovida = index
            print(index, valor)

        if (posicaoRemovida != -1):
            self.tuple = (*self.tuple[0: posicaoRemovida - 1],
                          *self.tuple[posicaoRemovida + 1: -1])
            print(self.tuple)

    # def sort(self):
    #     self.tupla = self.tupla

    # def reverse(self):
    #     self.tupla = self.tupla

    # def pop(self, index = -1):
    #     # TBD
    #     self.tupla = self.tupla[:index]

    def printObj(self):
        print(self.tuple)


def main():
    minha_lista = MinhaLista([1, 2, 3, 4, 5])

    # minha_lista.append(1)
    minha_lista.remove(3)


main()
