from DAOs.dao import DAO
from entidade.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if ((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str)):
            super().add(aluno.cpf, aluno)

    def update(self, aluno: Aluno):
        if ((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.cpf, str)):
            super().update(aluno.cpf, aluno)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
