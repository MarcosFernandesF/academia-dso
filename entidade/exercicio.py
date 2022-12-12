from entidade.aparelho import Aparelho


class Exercicio:
    def __init__(self, nome: str, aparelho: Aparelho, id_exercicio: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(aparelho, Aparelho):
            self.__aparelho = aparelho
        if isinstance(id_exercicio, str):
            self.__id_exercicio = id_exercicio
        
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
        
    @property
    def id_exercicio(self) -> str:
        return self.__id_exercicio