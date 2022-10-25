from limite.tela_aparelho import TelaAparelho
from entidade.aparelho import Aparelho

class ControladorAparelhos():

    def __init__(self):
        self.__tela_aparelhos = TelaAparelho()
        self.__aparelhos = []

    def inicial(self):
        self.abre_tela_inicial()

    def criar_grupoMuscular(nome: str):
        pass

    def listar_aparelhos(self):
        pass

    def finalizar(self):
        pass

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.listar_aparelhos
            }

        while True:
            opcao = self.__tela_aparelho.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()