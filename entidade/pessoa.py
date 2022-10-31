from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, sexo: str, cpf: str):
        if isinstance(nome, str) and isinstance(sexo, str) and isinstance(cpf, str):
            self.__nome = nome
            self.__sexo = sexo
            self.__cpf = cpf
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def sexo(self) -> str:
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        if isinstance(sexo, str):
            self.__sexo = sexo
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    
