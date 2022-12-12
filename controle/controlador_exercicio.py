from limite.tela_exercicio import TelaExercicio
from entidade.exercicio import Exercicio
from exception.menu_not_found_error import MenuNotFoundError

class ControladorExercicio():

    def __init__(self, controlador_sistema):
        self.__tela_exercicio = TelaExercicio()
        self.__controlador_sistema = controlador_sistema
        self.__exercicios = []
    
    @property
    def exercicios(self):
        return self.__exercicios
    
    @exercicios.setter
    def exercicios(self, exercicios):
        self.__exercicios = exercicios

    def pega_exercicio_por_id(self, id: str):
        
        for exercicio in self.__exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio
        raise ValueError(">>>Ocorreu uma exceção ValueError")

    def criar_exercicio(self):
        try:
            dados_exercicio = self.__tela_exercicio.pega_dados_exercicio()
            aparelho = self.__controlador_sistema.controlador_aparelho.pega_aparelho_por_id(dados_exercicio["id_aparelho"])
            if aparelho == False:
                raise ValueError
            exercicio = Exercicio(dados_exercicio["nome"], aparelho, self.__controlador_sistema.cria_id())
            self.__exercicios.append(exercicio)

        except TypeError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>O nome possui um tipo diferente do que deveria ter!")          
            self.__tela_exercicio.mostra_mensagem(">>>nome[str]\n")

        except ValueError as e:
            self.__tela_exercicio.mostra_mensagem(e)
            self.__tela_exercicio.mostra_mensagem(">>>Não existe Aparelho com este ID")          

    def modificar_exercicio(self):
        try:
            if len(self.__exercicios) > 0:
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
        else:
            self.__tela_exercicio.mostra_mensagem("-------- LISTA DE EXERCÍCIOS --------")
            for exercicio in self.__exercicios:
                print("============")
                print(f"Nome do exercício: {exercicio.nome}")
                print(f"ID do exercício: {exercicio.id_exercicio}")
                print(f"ID do aparelho utilizado: {exercicio.aparelho.id}\n")
        
    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        lista_opcoes = {
            0: self.retornar, 
            1: self.criar_exercicio, 
            2: self.modificar_exercicio, 
            3:  self.listar_exercicios, 
            4: self.excluir_exercicio
            }

        while (True):
            try:
                lista_opcoes[self.__tela_exercicio.tela_opcoes()]()
            except MenuNotFoundError as e:
                self.__tela_exercicio.mostra_mensagem(e)

