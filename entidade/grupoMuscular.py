from exercicio import Exercicio

class GrupoMuscular:
    def __init__(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome