from entidade.exercicio import Exercicio
from entidade.instrutor import Instrutor


class Treino:
    def __init__(self, nome: str, exercicio: Exercicio, duracao: int, instrutor: Instrutor, id: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(id, str):
            self.__id = id
        if isinstance(duracao, int):
            self.__duracao = duracao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def duracao(self) -> int:
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao: int):
        if isinstance(duracao, int):
            self.__duracao = duracao
    
    @property
    def id(self) -> str:
        return self.__id
    
    


    