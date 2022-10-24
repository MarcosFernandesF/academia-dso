from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def seleciona_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, mensagem):
        print(mensagem)
