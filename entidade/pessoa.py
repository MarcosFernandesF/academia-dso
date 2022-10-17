from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, sexo: str, cpf: str):
        if isinstance(nome, sexo, cpf, str):
            self.__nome = nome
            self.__sexo = sexo
            self.__cpf = cpf
        else:
            raise ... ##Criar exceção
    
    ##Por enquanto só setter para o nome
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ... ##Criar exceção

    @property
    def sexo(self) -> str:
        return self.__sexo

    @property
    def cpf(self) -> str:
        return self.__cpf

    
