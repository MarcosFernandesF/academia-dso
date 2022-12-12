from limite.tela_grupoMuscular import TelaGrupoMuscular
from entidade.grupoMuscular import GrupoMuscular

class ControladorGrupoMuscular():

    def __init__(self, controlador_sistema):
        self.__tela_grupoMuscular = TelaGrupoMuscular()
        self.__gruposmusculares = {}
        self.__controlador_sistema = controlador_sistema

    def inicial(self):
        self.abre_tela_inicial()

    def criar_grupoMuscular(self):
        dados_grupo_muscular = self.__tela_grupoMuscular.pega_dados_grupo_muscular()
        grupo_criado = GrupoMuscular(dados_grupo_muscular["Nome"], self.__controlador_sistema.cria_id())
        self.__gruposmusculares[grupo_criado] = []
        self.listar_grupos()

    def escolher_grupo_muscular(self):
        self.__tela_grupoMuscular.mostra_opcoes_grupo_muscular()

    def pega_grupo_muscular_por_id(self, id):
        for grupo in self.__gruposmusculares.keys():
            if (grupo.id == id):
                return grupo
        else:
            print("Grupo não existente")
            return None

    def pega_exercicio_por_id(self, id: str):
        controlador_exercicio = self.__controlador_sistema.controlador_exercicio
        lista_de_exercicios = controlador_exercicio.exercicios
        for exercicio in lista_de_exercicios:
            if(exercicio.id_exercicio == id):
                return exercicio.nome
            return None

    def incluir_exercicio(self):
        self.listar_grupos()
        id = self.__tela_grupoMuscular.pega_id_grupo_muscular()
        grupo_escolhido = self.pega_grupo_muscular_por_id(id)
        codigo_exercicio = self.__tela_grupoMuscular.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)
        self.__gruposmusculares[grupo_escolhido].append(exercicio_selecionado)
    
    def retirar_exercicio(self):
        self.listar_grupos()
        id = self.__tela_grupoMuscular.pega_id_grupo_muscular()
        grupo_escolhido = self.pega_grupo_muscular_por_id(id)
        codigo_exercicio = self.__tela_grupoMuscular.seleciona_exercicio()
        exercicio_selecionado = self.pega_exercicio_por_id(codigo_exercicio)
        self.__gruposmusculares[grupo_escolhido].remove(exercicio_selecionado)

    def listar_grupos(self):
        print("\nGrupos Musculares cadastrados:")
        for i in self.__gruposmusculares.keys():
            self.__tela_grupoMuscular.mostra_grupo_muscular(i)

    def listar_exercicios_por_grupo(self):
        id = self.__tela_grupoMuscular.pega_id_grupo_muscular()
        grupo_selecionado = self.pega_grupo_muscular_por_id(id)
        for grupo in self.__gruposmusculares.keys():
            if (grupo == grupo_selecionado):
                print(f"\nExercicios cadastrados no grupo {grupo_selecionado.nome}:")
                for i in range(len(self.__gruposmusculares[grupo_selecionado])):
                    print(f"Exercício {i}: {self.__gruposmusculares[grupo_selecionado][i]}")

    def modificar_grupo(self):
        id = self.__tela_grupoMuscular.pega_id_grupo_muscular()
        grupo_selecionado = self.pega_grupo_muscular_por_id(id)
        for grupo in self.__gruposmusculares.keys():
            if (grupo == grupo_selecionado):
                novos_dados = self.__tela_grupoMuscular.pega_dados_grupo_muscular()
                grupo_selecionado.nome = novos_dados["Nome"]
    
    def remover_grupo(self):
        id = self.__tela_grupoMuscular.pega_id_grupo_muscular()
        grupo_selecionado = self.pega_grupo_muscular_por_id(id)
        for grupo in list(self.__gruposmusculares.keys()):
            if (grupo == grupo_selecionado):
                del self.__gruposmusculares[grupo_selecionado]
                print("Exclusão feita com sucesso!\n")

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 
            1: self.incluir_exercicio, 
            2: self.retirar_exercicio,
            3: self.listar_exercicios_por_grupo, 
            4: self.criar_grupoMuscular, 
            5: self.listar_grupos,
            6: self.modificar_grupo,
            7: self.remover_grupo
            }

        while True:
            opcao = self.__tela_grupoMuscular.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()