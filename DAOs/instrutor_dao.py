from dao import DAO
from entidade.instrutor import Instrutor

class instrutorDAO(DAO):
    def __init__(self):
        super().__init__('instrutors.pkl')

    def add(self, instrutor: Instrutor):
        if ((instrutor is not None) and isinstance(instrutor, Instrutor) and isinstance(instrutor.cpf, str)):
            super().add(instrutor.cpf, instrutor)

    def update(self, instrutor: Instrutor):
        if ((instrutor is not None) and isinstance(instrutor, Instrutor) and isinstance(instrutor.cpf, str)):
            super().update(instrutor.cpf, instrutor)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, str)):
            return super().remove(key)
