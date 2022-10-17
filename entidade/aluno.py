from pessoa import Pessoa
from plano import Plano

class Aluno(Pessoa):
    def __init__(self, nome: str, sexo: str, cpf: str, plano: Plano):
        super().__init__(nome, sexo, cpf)
        if isinstance(plano, Plano):
            self.__plano = plano
        else:
            raise ... ##Criar exceção
        
    @property
    def plano(self) -> str:
        return self.__plano
