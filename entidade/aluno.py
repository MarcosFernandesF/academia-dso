from entidade.pessoa import Pessoa
from entidade.plano import Plano

class Aluno(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, plano: Plano):
        super().__init__(nome, sexo, cpf)
        if isinstance(plano, Plano):
            self.__plano = plano
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
        
    @property
    def plano(self) -> str:
        return self.__plano

    @plano.setter
    def plano(self, plano):
        if isinstance(plano, Plano):
            self.__plano = plano
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

