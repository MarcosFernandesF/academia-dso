from limite.tela_grupoMuscular import TelaGrupoMuscular
from entidade.grupoMuscular import GrupoMuscular

class ControladorGrupoMuscular():

    def __init__(self, controlador_sistema):
        self.__tela_grupoMuscular = TelaGrupoMuscular()
        self.__gruposmusculares = {}
        self.__controlador_sistema = controlador_sistema

    def inicial(self):
        self.abre_tela_inicial()

    def criar_grupoMuscular(self, nome: str):
        self.__gruposmusculares.keys(nome) #verificar se metodo keys esta correto

    def adicionar_exercicio(self):
        print("adicionando")

    def retirar_exercicio(self):
        pass

    def listar_exercicios_por_grupo(self):
        pass

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.adicionar_exercicio, 2: self.retirar_exercicio,
            3: self.listar_exercicios_por_grupo}

        while True:
            opcao = self.__tela_grupoMuscular.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()