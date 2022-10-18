from exercicio import Exercicio


class Treino:
    def __init__(self, nome: str, exercicios: Exercicio, duracao: int, instrutor: Instrutor):
        if isinstance(nome, str):
            self.__nome = nome
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
    def duracao(self, duracao: Duracao):
        if isinstance(duracao, Duracao):
            self.__duracao = duracao
    
    


    