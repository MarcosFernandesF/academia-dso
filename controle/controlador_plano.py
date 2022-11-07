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
        if isinstance(plano, Plano):
            self.__planos.append(plano)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    def cria_plano(self, nome: str, duracao: str, preco: float) -> object:
        try:
            plano = Plano(nome, duracao, preco)
            return plano
        except TypeError:
            self.__tela_plano.mostra_mensagem(">>>Alguma das entradas estão com o tipo diferente do que deveriam estar!")          
            self.__tela_plano.mostra_mensagem(">>>nome[str], duracao[str], preco[float]")

    def lista_planos(self):
        for plano in self.__planos:
            self.__tela_plano.mostra_plano({"nome": plano.nome, "duracao": plano.duracao, "preco": plano.preco})