from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        Mamifero.__init__(self, 2, 2)

    def miar(self):
        return f"MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: MIAU"

    def produzir_som(self):
        return self.miar()
