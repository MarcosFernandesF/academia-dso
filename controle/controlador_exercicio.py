from limite.tela_exercicio import TelaExercicio
from entidade.exercicio import Exercicio

class ControladorExercicio():

    def __init__(self, controlador_sistema):
        self.__tela_exercicio = TelaExercicio()
        self.__controlador_sistema = controlador_sistema
        self.__exercicios = []

    def inicial(self):
        self.abre_tela_inicial()

    def pega_exercicio_por_id(self, id: str):
        for exercicio in self.__exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio
            return None

    def incluir_exercicio(self):
        dados_exercicio = self.__tela_exercicio.pega_dados_exercicio()
        aparelho = self.__controlador_sistema.controlador_aparelho.pega_aparelho_por_id(dados_exercicio["id"])
        exercicio = Exercicio(dados_exercicio["nome"], aparelho, dados_exercicio["id_exercicio"])
        self.__exercicios.append(exercicio)

    def listar_exercicios(self):
        print("<-------- LISTANDO EXERCICIOS ------->")
        for exercicio in self.__exercicios:
            self.__tela_exercicio.mostra_exercicio(
                {
                "nome": exercicio.nome, 
                "aparelho": exercicio.aparelho.nome, #corrigir print do nome do aparelho
                "id_exercicio": exercicio.id_exercicio, 
                }
            )
    
    def excluir_exercicio(self):
        codigo_exercicio = self.__tela_exercicio.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)

        if(exercicio_selecionado is not None):
            self.__exercicios.remove(exercicio_selecionado)
            print("Exercicio removido")
        else:
            pass #mostar mensagem de exercicio nao existente
    
    def modificar_exercicio(self):
        codigo_exercicio = self.__tela_exercicio.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)

        if (exercicio_selecionado is not None):
            novos_dados_exercicio = self.__tela_exercicio.pega_dados_exercicio()
            exercicio_selecionado.nome = novos_dados_exercicio["nome"]
            exercicio_selecionado.aparelho = novos_dados_exercicio["id"]
            exercicio_selecionado.id_exercicio = novos_dados_exercicio["id_exercicio"]
        else:
            pass #mostrar mensagem de exercicio nao existente
        

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.incluir_exercicio, 2: self.modificar_exercicio, 3:self.excluir_exercicio, 4: self.listar_exercicios
            }

        while True:
            opcao = self.__tela_exercicio.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
