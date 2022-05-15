from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self):
        Mamifero.__init__(self, 3, 3)

    def latir(self):
        return f"MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU"

    def produzir_som(self):
        return self.latir()
