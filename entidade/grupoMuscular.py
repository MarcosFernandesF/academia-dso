#importtar exercicio

class GrupoMuscular:
    def __init__(self, nome: str, id: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(id, str):
            self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def id(self) -> str:
        return self.__id