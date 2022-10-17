from time import strftime
from pessoa import Pessoa
from aluno import Aluno

class Instrutor(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, cref: str):
        super().__init__(nome, sexo, cpf)
        if isinstance(cref, str):
            self.__cref = cref
            self.__alunos = []
        else:
            raise ... #Criar exceção

    @property
    def cref(self) -> str:
        return self.__cref

    @property
    def alunos(self) -> list:
        return self.__alunos