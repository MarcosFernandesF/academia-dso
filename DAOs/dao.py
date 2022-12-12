import pickle
from abc import ABC, abstractmethod
import entidade

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} 
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  #atualiza o arquivo depois de add novo amigo

    #cuidado: esse update só funciona se o objeto com essa chave já existe
    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                if isinstance(obj, entidade.instrutor.Instrutor) or isinstance(obj, entidade.aluno.Aluno):
                    self.__cache[key] = obj #atualiza a entrada 
                    self.__cache[obj.cpf] = self.__cache.pop(key) 
                    self.__dump()  #atualiza o arquivo
                elif isinstance(obj, entidade.plano.Plano):
                    self.__cache[key] = obj #atualiza a entrada 
                    self.__cache[obj.nome] = self.__cache.pop(key) 
                    self.__dump()  #atualiza o arquivo
        except KeyError:
            print("Update falhou - KeyError")

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass #implementar aqui o tratamento da exceção

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() #atualiza o arquivo depois de remover um objeto
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()