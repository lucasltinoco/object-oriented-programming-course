from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    '''
    Retorna o baralho
    @return o baralho
    '''
    @property
    def baralho(self) -> list:
        return self.__baralho

    '''
    Retorna a lista de personagems
    @return a lista de personagems
    '''
    @property
    def personagems(self) -> list:
        return self.__personagens

    '''
    Permite incluir um novo Personagem na lista de personagens do jogo
    @param energia Energia do novo Personagem
    @param habilidade Habilidade do novo Personagem
    @param velocidade Velocidade do novo Personagem
    @param resistencia Resistencia do novo Personagem
    @param tipo TipoPersonagem (Enum) do novo Personagem.
    Deve ser utilizado TipoPersonagem.TIPO
    @return Retorna o Personagem incluido na lista
    '''

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if isinstance(tipo, Tipo):
            personagem = Personagem(energia, habilidade, velocidade,
                                    resistencia, tipo)
            self.__personagens.append(personagem)
            return personagem

    '''
     Permite incluir uma nova Carta no baralho do jogo
     @param personagem Personagem da nova carta que sera incluida
     @return Retorna a Carta que foi incluida no baralho
     '''

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if personagem in self.__personagens:
            carta = Carta(personagem)
            self.baralho.append(carta)
            return carta

    '''
    Inicia o jogo, distribuindo aleatoriamente 5 cartas do baralho
    para cada jogador, a distribuicao nao precisa ser aleatoria

    @param jogador1 Jogador 1
    @param jogador2 Jogador 2
    '''

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        if isinstance(jogador1, Jogador) and isinstance(jogador2, Jogador):
            for i in range(0, 5):
                jogador1.inclui_carta_na_mao(
                    self.baralho[random.randint(0, len(self.baralho))])
                jogador2.inclui_carta_na_mao(
                    self.baralho[random.randint(0, len(self.baralho))])

    '''
     Realiza uma jogada, ou seja:
     1. Recebe a mesa onde estao as cartas lancadas pelo Jogador 1
     e pelo Jogador 2
     2. Compara os valores totais das cartas dos jogadores que estao
     na mesa
     3. Apos comparacao:

     O jogador que ganhar a rodada recebe a carta do jogador perdedor
     sendo assim ele deve chamar o metodo inclui_carta_na_mao para as
     duas cartas que estao na mesa

     Caso ocorra empate ambos os jogadores devem chamar o metodo
     inclui_carta_na_mao com suas respectivas cartas da mesa

     4.Ao final do metodo o jogador que estiver com a mao vazia
     perde o jogo, caso ambos ainda tenham cartas na mao retorne
     None para indicar que por enquanto ninguem venceu o jogo.

     @param mesa Mesa atual, contendo: Jogador 1, Jogador 2,
     Carta do Jogador 1 e Carta do Jogador 2
     @return Retorna o Jogador vencedor da rodada.
     Caso ocorra empate entre os jogadores, retorna None
     '''

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            jogador1_vence = mesa.carta_jogador1.valor_total_carta(
            ) > mesa.carta_jogador2.valor_total_carta()

            jogador2_vence = mesa.carta_jogador1.valor_total_carta(
            ) < mesa.carta_jogador2.valor_total_carta()

            if (jogador1_vence):
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            elif (jogador2_vence):
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            else:
                mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
                mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)

            if len(mesa.jogador1.mao) == 0:
                return mesa.jogador2
            elif len(mesa.jogador2.mao) == 0:
                return mesa.jogador1
            else:
                return None
