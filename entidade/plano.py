#from entidade.aluno import Aluno

class Plano():
    def __init__(self, nome: str, duracao: str, preco: float, codigo: int):
        if isinstance(nome, duracao, str) and isinstance(preco, float) and isinstance(codigo, int):
            self.__nome = nome
            self.__duracao = duracao
            self.__preco = preco
            self.__codigo = codigo
        else:
            raise ... ##Criar exceção

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def duracao(self) -> str:
        return self.__duracao

    @property
    def preco(self) -> float:
        return self.__preco
    
    @property
    def codigo(self) -> int:
        return self.__codigo