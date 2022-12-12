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
        if isinstance(exercicio, Exercicio):
            self.__exercicio = exercicio
        if isinstance(instrutor, Instrutor):
            self.__instrutor = instrutor

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
    
    @property
    def exercicio(self) -> str:
        return self.__exercicio

    @exercicio.setter
    def exercicio(self, exercicio: str):
        if isinstance(exercicio, str):
            self.__exercicio = exercicio
    
    @property
    def instrutor(self) -> str:
        return self.__instrutor

    @instrutor.setter
    def instrutor(self, instrutor: str):
        if isinstance(instrutor, str):
            self.__instrutor = instrutor