from limite.tela_grupoMuscular import TelaGrupoMuscular
from entidade.grupoMuscular import GrupoMuscular

class ControladorGrupoMuscular():

    def __init__(self, controlador_sistema):
        self.__tela_grupoMuscular = TelaGrupoMuscular()
        self.__gruposmusculares = {}
        self.__controlador_sistema = controlador_sistema

    def inicial(self):
        self.abre_tela_inicial()

    def criar_grupoMuscular(self, nome: str):
        self.__gruposmusculares[nome] = []

    def escolher_grupo_muscular(self):
        self.__tela_grupoMuscular.mostra_opcoes_grupo_muscular()

    def pega_exercicio_por_id(self, id: str):
        controlador_exercicio = self.__controlador_sistema.controlador_exercicio
        lista_de_exercicios = controlador_exercicio.exercicios
        for exercicio in lista_de_exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio.nome
            return None
    
    def incluir_exercicio(self):
        switcher = {
            1: "Grupo Muscular Um",
            2: "Grupo Muscular Dois",
            3: "Grupo Muscular Tres",
            4: "Grupo Muscular Quatro",
            5: "Grupo Muscular Cinco"}
        escolha = self.__tela_grupoMuscular.mostra_opcoes_grupo_muscular()
        grupo_escolhido = switcher[escolha]
        codigo_exercicio = self.__tela_grupoMuscular.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)
        self.__gruposmusculares[grupo_escolhido].append(exercicio_selecionado)
    
    def retirar_exercicio(self):
        switcher = {
            1: "Grupo Muscular Um",
            2: "Grupo Muscular Dois",
            3: "Grupo Muscular Tres",
            4: "Grupo Muscular Quatro",
            5: "Grupo Muscular Cinco"}
        escolha = self.__tela_grupoMuscular.mostra_opcoes_grupo_muscular()
        grupo_escolhido = switcher[escolha]
        codigo_exercicio = self.__tela_grupoMuscular.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)
        self.__gruposmusculares[grupo_escolhido].remove(exercicio_selecionado)

    def listar_exercicios_por_grupo(self):
        escolha = self.__tela_grupoMuscular.seleciona_grupoMuscular()
        print(self.__gruposmusculares)

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.incluir_exercicio, 2: self.retirar_exercicio,
            3: self.listar_exercicios_por_grupo}

        while True:
            opcao = self.__tela_grupoMuscular.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()