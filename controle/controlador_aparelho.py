from limite.tela_aparelho import TelaAparelho
from entidade.aparelho import Aparelho
from exception.menu_not_found_error import MenuNotFoundError

class ControladorAparelhos():

    def __init__(self, controlador_sistema):
        self.__tela_aparelho = TelaAparelho()
        self.__controlador_sistema = controlador_sistema
        self.__aparelhos = []

    def inicial(self):
        self.abre_tela_inicial()

    def criar_aparelho(self):
        dados_aparelho = self.__tela_aparelho.pega_dados_aparelho()
        aparelho_criado = Aparelho(dados_aparelho["Nome"], self.__controlador_sistema.cria_id())
        self.__aparelhos.append(aparelho_criado)
        print("Aparelho criado com sucesso!")
    
    def modificar_aparelho(self):
        id = self.__tela_aparelho.pega_id_aparelho()
        aparelho_selecionado = self.pega_aparelho_por_id(id)
        for aparelho in self.__aparelhos.copy():
            if (aparelho == aparelho_selecionado):
                novos_dados = self.__tela_aparelho.pega_dados_aparelho()
                aparelho.nome = novos_dados["Nome"]
                print("Nome modificado com sucesso!")
    
    def excluir_aparelho(self):
        id = self.__tela_aparelho.pega_id_aparelho()
        aparelho_selecionado = self.pega_aparelho_por_id(id)
        for aparelho in self.__aparelhos.copy():
            if (aparelho == aparelho_selecionado):
                self.__aparelhos.remove(aparelho)
                print("Aparelho deletado com sucesso!")

    def listar_aparelhos(self):
        if len(self.__aparelhos) > 0:
            print("\nAparelhos cadastrados:")
            for aparelho in self.__aparelhos:
                print(f"Nome: {aparelho.nome} | ID: {aparelho.id}")
        else:
            print("Nenhum aparelho cadastrado!")

    def pega_aparelho_por_id(self, id: str):
        try:
            if len(self.__aparelhos) == 0:
                return False
            for aparelho in self.__aparelhos:
                if(aparelho.id == id):
                    return aparelho
            return False
            
        except ValueError as e:
            self.__tela_aparelho.mostra_mensagem(e)
            self.__tela_aparelho.mostra_mensagem(">>>Não existe Aparelho com este ID")

    def finalizar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finalizar, 
            1: self.listar_aparelhos,
            2: self.criar_aparelho,
            3: self.modificar_aparelho,
            4: self.excluir_aparelho,
            }

        while True:
            try:
                opcao = self.__tela_aparelhos.mostra_tela_opcoes()
                funcao_escolhida = switcher[opcao]
                funcao_escolhida()
            except MenuNotFoundError as e:
                self.__tela_aparelhos.mostra_mensagem(e)