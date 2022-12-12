from limite.tela_plano import TelaPlano
from entidade.plano import Plano
from DAOs.plano_dao import PlanoDAO

class ControladorPlano():
    
    def __init__(self, controlador_sistema):
        #self.__planos = []
        self.__plano_DAO = PlanoDAO()

        self.__tela_plano = TelaPlano()
        self.__controlador_sistema = controlador_sistema

    @property
    def plano_DAO(self):
        return self.__plano_DAO

    def pega_plano_por_nome(self, nome: str):
        for plano in self.__plano_DAO.get_all():
            if(plano.nome == nome):
                return plano
        else:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

    def incluir_plano(self):
        try:
            dados_plano = self.__tela_plano.pega_dados_plano()
            for plano in self.__plano_DAO.get_all():
                if dados_plano["nome"] == plano.nome:
                    self.__tela_plano.mostra_mensagem("Ja existe um plano com este nome!")
            else:
                plano = Plano(dados_plano["nome"], dados_plano["duracao"], dados_plano["preco"])
                self.__plano_DAO.add(plano)

            return plano
        except TypeError:
            self.__tela_plano.mostra_mensagem(">>>Alguma das entradas estão com o tipo diferente do que deveriam estar!")          
            self.__tela_plano.mostra_mensagem(">>>nome[str], duracao[str], preco[float]")
        except ValueError as e:
            self.__tela_plano.mostra_mensagem(e)
            self.__tela_plano.mostra_mensagem(">>>A entrada 'Duração' foi escrita de maneira errada!")          
            self.__tela_plano.mostra_mensagem(">>>Maneira certa: Mensal / Semestral / Anual\n")

    def alterar_plano(self):
        try:
            if (self.lista_planos()) is not None:
                nome_plano = self.__tela_plano.seleciona_plano()
                plano = self.pega_plano_por_nome(nome_plano)

                novos_dados_plano = self.__tela_plano.pega_dados_plano()
                plano.nome = novos_dados_plano["nome"]
                plano.duracao = novos_dados_plano["duracao"]
                plano.preco = novos_dados_plano["preco"]

                self.__plano_DAO.update(nome_plano, plano)

        except TypeError as e:
            self.__tela_plano.mostra_mensagem(">>>Alguma das entradas estão com o tipo diferente do que deveriam estar!")          
            self.__tela_plano.mostra_mensagem(">>>nome[str], duracao[str], preco[float]")
        except ValueError as e:
            self.__tela_plano.mostra_mensagem(e)
            self.__tela_plano.mostra_mensagem(">>>Não existe plano com este nome")    
            self.__tela_plano.mostra_mensagem(">>>OU")
            self.__tela_plano.mostra_mensagem(">>>A entrada 'Duração' foi escrita de maneira errada!")          
            self.__tela_plano.mostra_mensagem(">>>Maneira certa: Mensal / Semestral / Anual\n")

    def excluir_plano(self):
        try:
            if (self.lista_planos()) is not None:
                nome_plano = self.__tela_plano.seleciona_plano()
                
                self.__plano_DAO.remove(nome_plano)
                self.lista_planos()

        except ValueError as e:
            self.__tela_plano.mostra_mensagem(e)
            self.__tela_plano.mostra_mensagem(">>>Não há nenhum plano com este nome!\n") 

    def lista_planos(self):
        if len(self.__plano_DAO.get_all()) == 0:
                self.__tela_plano.mostra_mensagem("ATENÇÃO: Não existe nenhum plano\n")
                return None
        else:
            self.__tela_plano.mostra_mensagem("---------- LISTA DE PLANOS ----------")
            for plano in self.__plano_DAO.get_all():
                self.__tela_plano.mostra_plano({"nome": plano.nome, "duracao": plano.duracao, "preco": plano.preco})
            return True

    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_plano, 2: self.alterar_plano, 3: self.lista_planos, 4: self.excluir_plano, 0: self.retornar}

        while (True):
            try:
                lista_opcoes[self.__tela_plano.tela_opcoes()]()
            except ValueError as e:
                self.__tela_plano.mostra_mensagem(e)
                self.__tela_plano.mostra_mensagem(">>>O valor digitado não corresponde as opções\n")