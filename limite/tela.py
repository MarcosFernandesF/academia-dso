from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def mostra_mensagem(self, mensagem):
        print(mensagem)
