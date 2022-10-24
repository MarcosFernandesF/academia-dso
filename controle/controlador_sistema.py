from controle.controlador_instrutor import ControladorInstrutor
from controle.controlador_aluno import ControladorAluno

class ControladorSistema:

    def __init__(self):
        self.__controlador_instrutor = ControladorInstrutor(self)
        self.__controlador_aluno = ControladorAluno(self)

    @property
    def controlador_instrutor(self):
        return self.__controlador_instrutor

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    def cadastra_instrutores(self):
        self.__controlador_instrutor.abre_tela()

    def abre_tela(self):
        pass