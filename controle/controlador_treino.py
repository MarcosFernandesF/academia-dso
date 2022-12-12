from limite.tela_treino import TelaTreino
from entidade.treino import Treino

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
        if instrutor is not None:
            treino = Treino(dados_treino["nome"], exercicio, dados_treino["duracao"], instrutor, self.__controlador_sistema.cria_id())  
            self.__treinos.append(treino)
            print("Treino criado!")
        else:
            print("Instrutor não existe!")

    def escolher_grupo_muscular(self):
        self.__tela_Treino.mostra_opcoes_grupo_muscular()

    def pega_exercicio_por_id(self, id: str):
        controlador_exercicio = self.__controlador_sistema.controlador_exercicio
        lista_de_exercicios = controlador_exercicio.exercicios
        for exercicio in lista_de_exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio.nome
            return None
    
    def pega_treino_por_id(self, id: str):
        for treino in self.__treinos:
            if(treino.id == id):
                return treino
        else:
            return None

    def modificar_treino(self):
        id_selecionado = self.__tela_Treino.seleciona_treino()
        treino_selecionado = self.pega_treino_por_id(id_selecionado)

        if (treino_selecionado is not None):
            novos_dados_treino = self.__tela_Treino.pega_dados_treino()
            if novos_dados_treino["cref"] is not None:
                treino_selecionado.nome = novos_dados_treino["nome"]
                treino_selecionado.exercicio = self.__controlador_sistema.controlador_exercicio.pega_exercicio_por_id(novos_dados_treino["id_exercicio"])
                treino_selecionado.duracao = novos_dados_treino["duracao"]
                treino_selecionado.instrutor = self.__controlador_sistema.controlador_instrutor.pega_instrutor_por_cref(novos_dados_treino["cref"])
                print("Treino modificado!")
            else:
                print("Instrutor não existente!")
        else:
            print("Treino não existente!")
    
    def listar_treino(self):
        if len(self.__treinos) > 0: 
            for treino in self.__treinos:
                print("============")
                print(f"Nome do treino: {treino.nome}")
                print(f"Nome do exercício: {treino.exercicio.nome}")
                print(f"Duração em minutos: {treino.duracao}")
                print(f"Instrutor: {treino.instrutor.nome}")
                print(f"ID do treino: {treino.id}")
        else:
            print("Não há treinos existentes!")
    
    def remover_treino(self):
        if len(self.__treinos) > 0:
            id_selecionado = self.__tela_Treino.seleciona_treino()
            treino_selecionado = self.pega_treino_por_id(id_selecionado)
            if treino_selecionado is not None:
                self.__treinos.remove(treino_selecionado)
                print("Treino excluido!")
            else:
                print("Não existe um treino com este ID")
        else:
            print("Não há treinos cadastrados!")

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 1: self.criar_Treino, 2: self.modificar_treino, 3:self.remover_treino, 4: self.listar_treino}

        while True:
            opcao = self.__tela_Treino.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()