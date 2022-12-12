from limite import tela_treino
from limite.tela_sistema import TelaSistema
from controle.controlador_grupoMuscular import ControladorGrupoMuscular
from controle.controlador_instrutor import ControladorInstrutor
from controle.controlador_aparelho import ControladorAparelhos
from controle.controlador_aluno import ControladorAluno
from controle.controlador_plano import ControladorPlano
from controle.controlador_treino import ControladorTreino
from controle.controlador_exercicio import ControladorExercicio

class ControladorSistema():

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_grupoMuscular = ControladorGrupoMuscular(self)
        self.__controlador_aparelhos = ControladorAparelhos(self)
        self.__controlador_exercicio = ControladorExercicio(self)
        self.__controlador_instrutor = ControladorInstrutor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_treino = ControladorTreino(self)
        self.__controlador_plano = ControladorPlano(self)
        self.__armazena_id = 0


    def inicia(self):
        self.abre_tela_inicial()

    def cadastra_alunos(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_instrutor(self):
        self.__controlador_instrutor.abre_tela()

    def cadastra_grupoMuscular(self):
        self.__controlador_grupoMuscular.abre_tela_inicial()
    
    def cadastra_planos(self):
        self.__controlador_plano.abre_tela()

    def tela_aparelhos(self):
        self.__controlador_aparelhos.abre_tela_inicial()

    def instancia_treino(self):
        treino = self.__controlador_treino.criar_treino()

    def tela_exercicio(self):
        self.__controlador_exercicio.abre_tela_inicial()
    
    def tela_treino(self):
        self.__controlador_treino.abre_tela_inicial()

    def abre_tela_inicial(self):
        lista_opcoes = {
            1: self.cadastra_alunos,
            2: self.cadastra_instrutor,
            3: self.cadastra_grupoMuscular,
            4: self.cadastra_planos,
            5: self.tela_aparelhos,
            6: self.tela_exercicio,
            7: self.tela_treino,
            0: self.encerra_sistema
        }

        while True:
            try:
                opcao = self.__tela_sistema.mostra_tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao]
                funcao_escolhida()
            except ModuleNotFoundError as e:
                self.__tela_sistema.mostra_mensagem(e)
    
    def encerra_sistema(self):
        exit(0)

    def cria_id(self):
    #Pega o id existente, incrementa um e armazena na variável id_exercício
        id_criado = self.__armazena_id + 1
    #Seta o id do controlador como o id novo gerado
        self.__armazena_id = id_criado
    #Retorna o id para a variável que chamou a função
        return str(id_criado)

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

    @property
    def controlador_exercicio(self):
        return self.__controlador_exercicio
    
    @property
    def armazena_id(self):
        return self.__armazena_id
    
    @armazena_id.setter
    def armazena_id(self, id):
        self.__armazena_id = id

