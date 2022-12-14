from DAOs.dao import DAO
from entidade.instrutor import Instrutor

class instrutorDAO(DAO):
    def __init__(self):
        super().__init__('instrutores.pkl')

    def add(self, instrutor: Instrutor):
        if ((instrutor is not None) and isinstance(instrutor, Instrutor) and isinstance(instrutor.cpf, str)):
            super().add(instrutor.cpf, instrutor)

    def update(self, cpf_instrutor: str, instrutor: Instrutor):
        if ((instrutor is not None) and isinstance(instrutor, Instrutor) and isinstance(cpf_instrutor, str) and cpf_instrutor is not None):
            super().update(cpf_instrutor, instrutor)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
