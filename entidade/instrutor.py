from entidade.pessoa import Pessoa
from DAOs.aluno_instrutor_dao import AlunoInstrutorDAO

class Instrutor(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, cref: str):
        super().__init__(nome, sexo, cpf)
        if isinstance(cref, str):
            self.__cref = cref
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

        self.__aluno_instrutor_DAO = AlunoInstrutorDAO()

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
    def aluno_instrutor_DAO(self) -> list:
        return self.__aluno_instrutor_DAO

    