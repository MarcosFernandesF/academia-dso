from limite.tela_plano import TelaPlano
from entidade.plano import Plano

class ControladorPlano():
    
    def __init__(self, controlador_sistema):
        self.__planos = []
        self.__tela_plano = TelaPlano()
        self.__controlador_sistema = controlador_sistema

    @property
    def planos(self):
        return self.__planos

    @planos.setter
    def planos(self, plano):
        self.__planos.append(plano)

    def cria_plano(self, nome: str, duracao: str, preco: float, codigo: int):
        plano = Plano(nome, duracao, preco, codigo)
        return plano

    def lista_planos(self):
        for plano in self.__planos:
            #Fazer tratamento de dados aqui ou em "mostra_plano"?
            self.__tela_plano.mostra_plano({"nome": plano.nome, "duracao": plano.duracao, "preco": plano.preco, "codigo": plano.codigo})