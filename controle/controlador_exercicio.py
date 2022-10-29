from limite.tela_exercicio import TelaExercicio
from entidade.exercicio import Exercicio

class ControladorExercicio():

    def __init__(self):
        self.__tela_exercicio = TelaExercicio()

    def inicial(self):
        self.abre_tela_inicial()
