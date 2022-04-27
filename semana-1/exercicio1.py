"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao():

    def __init__(self, array_para_ordenar: []):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        for i in range(len(self.array_para_ordenar)):
            for j in range(i + 1, len(self.array_para_ordenar)):
                if (self.array_para_ordenar[i] > self.array_para_ordenar[j]):
                    self.array_para_ordenar[i], self.array_para_ordenar[j] = self.array_para_ordenar[j], self.array_para_ordenar[i]

        return self.array_para_ordenar

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """

        return ','.join(map(str, self.array_para_ordenar))


def main():
    ordenacao = Ordenacao([1, 2, 3, 4, 5])

    print(ordenacao.ordena())
    print(ordenacao.toString())


main()
