from limite.tela_aparelho import TelaAparelho
from entidade.aparelho import Aparelho

class ControladorAparelhos():

    def __init__(self, controlador_sistema):
        self.__tela_aparelhos = TelaAparelho()
        self.__controlador_sistema = controlador_sistema
        self.__aparelhos = []

    def inicial(self):
        self.abre_tela_inicial()

    def criar_aparelho(self, nome: str, id: str):
        aparelho = Aparelho(nome, id)
        self.__aparelhos.append(aparelho)

    def pega_aparelho_por_id(self, id: str):
        for aparelho in self.__aparelhos:
            if(aparelho.id == id):
                return aparelho
            else:
                self.listar_aparelhos()
                raise ValueError

    def listar_aparelhos(self):
        print("\nAparelhos cadastrados:")
        for aparelhos in self.__aparelhos:
            print(f"Nome: {aparelhos.nome} | ID: {aparelhos.id}")

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.listar_aparelhos
            }

        while True:
            opcao = self.__tela_aparelhos.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()