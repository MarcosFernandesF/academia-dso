#from entidade.aluno import Aluno

class Plano():
    def __init__(self, nome: str, duracao: str, preco: float):
        if isinstance(nome, str) and isinstance(duracao, str) and isinstance(preco, float):
            self.__nome = nome
            self.__duracao = duracao
            self.__preco = preco
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome) -> str:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def duracao(self) -> str:
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao) -> str:
        if isinstance(duracao, str):
            self.__duracao = duracao
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco) -> float:
        if isinstance(preco, float):
            self.__preco = preco
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")