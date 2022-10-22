from controle.controlador_instrutor import ControladorInstrutor

class ControladorSistema:

    def __init__(self):
        self.__controlador_instrutor = ControladorInstrutor(self)

    def cadastra_instrutores(self):
        self.__controlador_instrutor.abre_tela()

    def abre_tela(self):
        pass