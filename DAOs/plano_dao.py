from DAOs.dao import DAO
from entidade.plano import Plano

class PlanoDAO(DAO):
    def __init__(self):
        super().__init__('planos.pkl')

    def add(self, plano: Plano):
        if ((plano is not None) and isinstance(plano, Plano) and isinstance(plano.nome, str)):
            super().add(plano.nome, plano)

    def update(self, nome_plano: str, plano: Plano):
        if ((plano is not None) and isinstance(plano, Plano) and isinstance(nome_plano, str) and nome_plano is not None):
            super().update(nome_plano, plano)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if(isinstance(key, str)):
            return super().remove(key)
