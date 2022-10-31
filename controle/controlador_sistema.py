from limite.tela_sistema import TelaSistema
from controle.controlador_grupoMuscular import ControladorGrupoMuscular
from controle.controlador_instrutor import ControladorInstrutor
from controle.controlador_aparelho import ControladorAparelhos
#from controle.controlador_aluno import ControladorAluno

class ControladorSistema():

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_grupoMuscular = ControladorGrupoMuscular(self)
        self.__controlador_aparelhos = ControladorAparelhos(self)
        self.__controlador_exercicio = ControladorExercicio(self)
        self.__controlador_instrutor = ControladorInstrutor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_plano = ControladorPlano(self)

    def inicia(self):
        self.abre_tela_inicial()

    def instancia_planos(self):
        plano_mensal = self.__controlador_plano.cria_plano("Plano Mensal", "1 Mês", 119.90, 1)
        self.__controlador_plano.planos = plano_mensal

        plano_semestral = self.__controlador_plano.cria_plano("Plano Semestral", "6 Meses", 109.90, 2)
        self.__controlador_plano.planos = plano_semestral

        plano_anual = self.__controlador_plano.cria_plano("Plano Anual", "12 Meses", 99.90, 3)
        self.__controlador_plano.planos = plano_anual

    def cadastra_alunos(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_instrutor(self):
        self.__controlador_instrutor.abre_tela()

    def cadastra_grupoMuscular(self):
        self.__controlador_grupoMuscular.abre_tela_inicial()
    
    def mostra_planos(self):
        pass

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
            3: self.cadastra_grupoMuscular, 5: self.tela_aparelhos
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

    @property
    def controlador_plano(self):
        return self.__controlador_plano

