class Aparelho:
    def __init__(self, nome: str, id: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(id, str):
            self.__id = id
        self.__exercicios = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def exercicios(self) -> list:
        return self.__exercicios

    @property
    def id(self) -> str:
        return self.__id