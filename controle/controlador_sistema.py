from limite.tela_sistema import TelaSistema
from controle.controlador_grupoMuscular import ControladorGrupoMuscular

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_grupoMuscular = ControladorGrupoMuscular()

    def inicia(self):
        self.abre_tela_inicial()

    def cadastra_grupoMuscular(self):
        self.__controlador_grupoMuscular.abre_tela_inicial()

    def abre_tela_inicial(self):
        lista_opcoes = {
            3: self.cadastra_grupoMuscular
        }

        while True:
            opcao = self.__tela_sistema.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()