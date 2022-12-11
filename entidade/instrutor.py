from entidade.pessoa import Pessoa
from entidade.aluno import Aluno
from DAOs.aluno_dao import AlunoDAO

class Instrutor(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, cref: str):
        super().__init__(nome, sexo, cpf)
        if isinstance(cref, str):
            self.__cref = cref
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

        self.__aluno_DAO = AlunoDAO()

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
    def aluno_DAO(self) -> list:
        return self.__aluno_DAO

    @aluno_DAO.setter
    def aluno_DAO(self, aluno):
        if isinstance(aluno, Aluno):
            self.__aluno_DAO.add(aluno)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    