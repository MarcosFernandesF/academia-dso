from exercicio import Exercicio


class Aparelho:
    def __init__(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        self.__exercicios = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def exercicios(self) -> list:
        return self.__exercicios