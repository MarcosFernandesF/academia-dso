from limite.tela_treino import TelaTreino
from entidade.treino import Treino
from exception.menu_not_found_error import MenuNotFoundError

class ControladorTreino():

    def __init__(self, controlador_sistema):
        self.__tela_Treino = TelaTreino()
        self.__treinos = []
        self.__controlador_sistema = controlador_sistema

    def inicial(self):
        self.abre_tela_inicial()

    def criar_Treino(self):
        dados_treino = self.__tela_Treino.pega_dados_treino()
        exercicio = self.__controlador_sistema.controlador_exercicio.pega_exercicio_por_id(dados_treino["id_exercicio"])
        instrutor = self.__controlador_sistema.controlador_instrutor.pega_instrutor_por_cref(dados_treino["cref"])
        treino = Treino(dados_treino["nome"], exercicio, dados_treino["duracao"], instrutor, dados_treino["id_treino"])  
        self.__treinos.append(treino)

    def escolher_grupo_muscular(self):
        self.__tela_Treino.mostra_opcoes_grupo_muscular()

    def pega_exercicio_por_id(self, id: str):
        controlador_exercicio = self.__controlador_sistema.controlador_exercicio
        lista_de_exercicios = controlador_exercicio.exercicios
        for exercicio in lista_de_exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio.nome
            return None

    def modificar_treino(self):
        codigo_exercicio = self.__tela_exercicio.seleciona_exercicio()
        treino_selecionado = self.pega_exercicio_por_id(codigo_exercicio)

        if (treino_selecionado is not None):
            novos_dados_treino = self.__tela_Treino.pega_dados_treino()
            treino_selecionado.nome = novos_dados_treino["nome"]
            treino_selecionado.duracao = novos_dados_treino["duracao"]
            treino_selecionado.duracao = novos_dados_treino["id_exercicio"]
            treino_selecionado.duracao = novos_dados_treino["cref"]
            treino_selecionado.id_treino = novos_dados_treino["id_treino"]
        else:
            print("Treino não existe")
    
    def listar_treino(self):
        print(self.__treinos)

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.criar_Treino, 2: self.modificar_treino, 3: self.listar_treino}

        while True:
            try:
                opcao = self.__tela_Treino.mostra_tela_opcoes()
                funcao_escolhida = switcher[opcao]
                funcao_escolhida()
            except MenuNotFoundError as e:
                self.__tela_Treino.mostra_mensagem(e)