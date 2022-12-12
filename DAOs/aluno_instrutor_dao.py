from DAOs.dao import DAO
from entidade.aluno import Aluno

class AlunoInstrutorDAO(DAO):
    def __init__(self):
        num_arquivo = str(Aluno.numero_arquivo)
        super().__init__('alunosinstrutor'+ num_arquivo +'.pkl') 
        Aluno.numero_arquivo += 1

    def add(self, aluno: Aluno):
        if ((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str)):
            super().add(aluno.cpf, aluno)

    def update(self, cpf_aluno: str, aluno: Aluno):
        if ((aluno is not None) and isinstance(aluno, Aluno) and isinstance(cpf_aluno, str) and cpf_aluno is not None):
            super().update(cpf_aluno, aluno)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
