from limite.tela_exercicio import TelaExercicio
from entidade.exercicio import Exercicio

class ControladorExercicio():

    def __init__(self, controlador_sistema):
        self.__tela_exercicio = TelaExercicio()
        self.__controlador_sistema = controlador_sistema
        self.__exercicios = []
        self.__id = 0

    def pega_exercicio_por_id(self, id: str):
        for exercicio in self.__exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio
        else:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

    def incluir_exercicio(self):
        try:    
            dados_exercicio = self.__tela_exercicio.pega_dados_exercicio()
            id_exercicio = self.cria_id()
            aparelho = self.__controlador_sistema.controlador_aparelho.pega_aparelho_por_id(id_exercicio)
            exercicio = Exercicio(dados_exercicio["nome"], aparelho, id_exercicio)
            self.__exercicios.append(exercicio)

        except TypeError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>O nome possui um tipo diferente do que deveria ter!")          
            self.__tela_exercicio.mostra_mensagem(">>>nome[str]\n")

        except ValueError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>Não existe Aparelho com este ID")          

    def alterar_exercicio(self):
        try:
            if (self.listar_exercicios()) is not None:
                id_exercicio = self.__tela_exercicio.seleciona_exercicio()
                exercicio = self.pega_exercicio_por_id(id_exercicio)

                novos_dados_exercicio = self.__tela_exercicio.pega_dados_exercicio()
                exercicio.nome = novos_dados_exercicio["nome"]
                exercicio.aparelho = novos_dados_exercicio["aparelho"]
        
        except TypeError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>O ID ou nome possui um tipo diferente do que deveria ter!")
            self.__tela_exercicio.mostra_mensagem(">>>id[int], nome[str]")
        except ValueError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>ID inválido!")          

    def excluir_exercicio(self):
        try:
            if (self.listar_exercicios()) is not None:
                id_exercicio = self.__tela_exercicio.seleciona_exercicio()
                exercicio = self.pega_exercicio_por_id(id_exercicio)

                self.__exercicios.remove(exercicio)
                self.listar_exercicios()
        
        except TypeError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>O ID digitado não possui o tipo adequado(int)")
        except ValueError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>Não há nenhum exercicio com este ID!\n") 

    def listar_exercicios(self):
        if len(self.__exercicios) == 0:
            self.__tela_exercicio.mostra_mensagem("ATENÇÃO: Não existe exercícios\n")
            return None
        else:
            self.__tela_exercicio.mostra_mensagem("-------- LISTA DE EXERCÍCIOS --------")
            for exercicio in self.__exercicios:
                #corrigir print do nome do aparelho
                self.__tela_exercicio.mostra_exercicio({"nome": exercicio.nome, "aparelho": exercicio.aparelho, "id_exercicio": exercicio.id_exercicio})
            return True

    def cria_id(self):
        #Pega o id existente, incrementa um e armazena na variável id_exercício
        id_exercicio = self.__id + 1
        #Seta o id do controlador como o id novo gerado
        self.__id = id_exercicio
        #Retorna o id para a variável que chamou a função
        return id_exercicio
    
    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        lista_opcoes = {
            0: self.retornar, 
            1: self.incluir_exercicio, 
            2: self.alterar_exercicio, 
            3: self.excluir_exercicio, 
            4: self.listar_exercicios
            }

        while (True):
            try:
                lista_opcoes[self.__tela_exercicio.tela_opcoes()]()
            except ValueError as e:
                self.__tela_exercicio.mostra_mensagem(e)
                self.__tela_exercicio.mostra_mensagem(">>>O valor digitado não corresponde as opções\n")

    @property
    def exercicios(self):
        return self.__exercicios

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id