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
    
    @property
    def duracao(self) -> str:
        return self.__duracao

    @property
    def preco(self) -> float:
        return self.__preco