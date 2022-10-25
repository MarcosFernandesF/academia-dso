from limite.tela_sistema import TelaSistema
from controle.controlador_grupoMuscular import ControladorGrupoMuscular
from controle.controlador_instrutor import ControladorInstrutor
from controle.controlador_aluno import ControladorAluno

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_grupoMuscular = ControladorGrupoMuscular()
        self.__controlador_instrutor = ControladorInstrutor(self)
        self.__controlador_aluno = ControladorAluno(self)

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

    @property
    def controlador_instrutor(self):
        return self.__controlador_instrutor

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    def cadastra_instrutores(self):
        self.__controlador_instrutor.abre_tela()

