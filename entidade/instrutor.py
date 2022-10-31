from entidade.pessoa import Pessoa
from entidade.aluno import Aluno

class Instrutor(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, cref: str):
        super().__init__(nome, sexo, cpf)
        if isinstance(cref, str):
            self.__cref = cref
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

        self.__alunos = []

    @property
    def cref(self) -> str:
        return self.__cref

    @cref.setter
    def cref(self, cref):
        if isinstance(cref, str):
            self.__cref = cref
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    @property
    def alunos(self) -> list:
        return self.__alunos

    @alunos.setter
    def alunos(self, aluno):
        if isinstance(aluno, Aluno):
            self.__alunos.append(aluno)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    