from aparelho import Aparelho


class Exercicio:
    def __init__(self, nome: str, aparelho: Aparelho):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(aparelho, Aparelho):
            self.__aparelho = Aparelho

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def aparelho(self) -> Aparelho:
        return self.__aparelho

    @aparelho.setter
    def aparelho(self, aparelho: Aparelho):
        if isinstance(aparelho, Aparelho):
            self.__aparelho = aparelho