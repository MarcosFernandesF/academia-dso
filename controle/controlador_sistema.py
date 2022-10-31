from limite.tela_sistema import TelaSistema
from controle.controlador_grupoMuscular import ControladorGrupoMuscular
from controle.controlador_instrutor import ControladorInstrutor
from controle.controlador_aparelho import ControladorAparelhos
from controle.controlador_exercicio import ControladorExercicio
#from controle.controlador_aluno import ControladorAluno

class ControladorSistema():

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_grupoMuscular = ControladorGrupoMuscular(self)
        self.__controlador_aparelhos = ControladorAparelhos(self)
        self.__controlador_exercicio = ControladorExercicio(self)
        self.__controlador_instrutor = ControladorInstrutor(self)
        #self.__controlador_aluno = ControladorAluno(self)

    def inicia(self):
        self.abre_tela_inicial()

    def cadastra_grupoMuscular(self):
        self.__controlador_grupoMuscular.abre_tela_inicial()

    def tela_aparelhos(self):
        self.__controlador_aparelhos.abre_tela_inicial()
    
    def instancia_aparelhos(self):
        aparelho_um = self.__controlador_aparelhos.criar_aparelho("Aparelho um", "1")
        aparelho_um = self.__controlador_aparelhos.criar_aparelho("Aparelho dois", "2")
        aparelho_um = self.__controlador_aparelhos.criar_aparelho("Aparelho três", "3")
        aparelho_um = self.__controlador_aparelhos.criar_aparelho("Aparelho quatro", "4")
        aparelho_um = self.__controlador_aparelhos.criar_aparelho("Aparelho cinco", "5")

    def tela_exercicio(self):
        self.__controlador_exercicio.abre_tela_inicial()

    def abre_tela_inicial(self):
        lista_opcoes = {
            3: self.cadastra_grupoMuscular, 5: self.tela_aparelhos, 6: self.tela_exercicio
        }

        while True:
            opcao = self.__tela_sistema.mostra_tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()

    @property
    def controlador_instrutor(self):
        return self.__controlador_instrutor

    @property
    def controlador_grupMuscular(self):
        return self.__controlador_grupoMuscular

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_aparelho(self):
        return self.__controlador_aparelhos

    def cadastra_instrutores(self):
        self.__controlador_instrutor.abre_tela()

