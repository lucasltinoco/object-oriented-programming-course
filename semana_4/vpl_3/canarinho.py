from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        Ave.__init__(self, tamanho_passo, altura_voo)

    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"

    def produzir_som(self):
        return self.cantar()
