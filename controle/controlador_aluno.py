from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno

class ControladorAluno():
    
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    @property
    def tela_aluno(self):
        return self.__tela_aluno

    def verifica_plano(self, lista_de_planos: list, dados_aluno: dict):
        if (dados_aluno["plano"]) == "Mensal":
            plano = lista_de_planos[0]
            return plano

        if (dados_aluno["plano"]) == "Semestral":
            plano = lista_de_planos[1]
            return plano

        if (dados_aluno["plano"]) == "Anual":
            plano = lista_de_planos[2]
            return plano


    def pega_aluno_por_cpf(self, cpf: str):
        for aluno in self.__alunos:
            if(aluno.cpf == cpf):
                return aluno
        return None

    #Fazer tratamento dos dados no "pega_dados_instrutor"
    def incluir_aluno(self):
        controlador_plano = self.__controlador_sistema.controlador_plano
        lista_de_planos = controlador_plano.planos

        dados_aluno = self.__tela_aluno.pega_dados_aluno()

        dados_aluno["plano"] = self.verifica_plano(lista_de_planos, dados_aluno)

        aluno = Aluno(dados_aluno["nome"], dados_aluno["sexo"], dados_aluno["cpf"], dados_aluno["plano"])
        self.__alunos.append(aluno)

    def alterar_aluno(self):
        if (self.lista_alunos()) is not None:
            cpf_aluno = self.__tela_aluno.seleciona_aluno()
            aluno = self.pega_aluno_por_cpf(cpf_aluno)

            #Utilizar exception aqui ou nao?
            #Utilizar raise no retorno de "pega_instrutuor_por_cpf"?
            if (aluno is not None):
                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
                lista_de_planos = self.__controlador_sistema.controlador_plano.planos

                novos_dados_aluno["plano"] = self.verifica_plano(lista_de_planos, novos_dados_aluno)

                aluno.nome = novos_dados_aluno["nome"]
                aluno.sexo = novos_dados_aluno["sexo"]
                aluno.cpf = novos_dados_aluno["cpf"]
                aluno.plano = novos_dados_aluno["plano"]
            else:
                self.__tela_aluno.mostra_mensagem("ATENÇÃO: Não há aluno com este CPF!\n")

    def excluir_aluno(self):
        if (self.lista_alunos()) is not None:
            cpf_aluno = self.__tela_aluno.seleciona_aluno()
            aluno = self.pega_aluno_por_cpf(cpf_aluno)

            if(aluno is not None):
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso! \n")
            else:
                self.__tela_aluno.mostra_mensagem("ATENÇÃO: Não há aluno com este CPF!\n")

    def lista_alunos(self):
        if len(self.__alunos) == 0:
            self.__tela_aluno.mostra_mensagem("ATENÇÃO: Não existe alunos cadastrados\n")
            return None
        else:
            self.__tela_aluno.mostra_mensagem("---------- LISTA DE ALUNOS ----------")
            for aluno in self.__alunos:
                #Fazer tratamento de dados aqui ou em "mostra_aluno"?
                self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "sexo": aluno.sexo, "cpf": aluno.cpf, "plano": aluno.plano})
            return True

    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 0: self.retornar}

        while (True):
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
