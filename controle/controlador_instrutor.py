from limite.tela_instrutor import TelaInstrutor
from entidade.instrutor import Instrutor

class ControladorInstrutor():
    
    def __init__(self, controlador_sistema):
        self.__instrutores = []
        self.__tela_instrutor = TelaInstrutor()
        self.__controlador_sistema = controlador_sistema

    def pega_instrutor_por_cpf(self, cpf: str):
        for instrutor in self.__instrutores:
            if(instrutor.cpf == cpf):
                return instrutor
        return None

    #Fazer tratamento dos dados no "pega_dados_instrutor"
    def incluir_instrutor(self):
        dados_instrutor = self.__tela_instrutor.pega_dados_instrutor()
        instrutor = Instrutor(dados_instrutor["nome"], dados_instrutor["sexo"], dados_instrutor["cpf"], dados_instrutor["cref"])
        self.__instrutores.append(instrutor)

    def alterar_instrutor(self):
        self.lista_instrutores()
        cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
        instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

        #Utilizar exception aqui ou nao?
        #Utilizar raise no retorno de "pega_instrutuor_por_cpf"?
        if (instrutor is not None):
            novos_dados_instrutor = self.__tela_instrutor.pega_dados_instrutor()
            instrutor.nome = novos_dados_instrutor["nome"]
            instrutor.sexo = novos_dados_instrutor["sexo"]
            instrutor.cpf = novos_dados_instrutor["cpf"]
            instrutor.cref = novos_dados_instrutor["cref"]
        else:
            self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Instrutor não existente")

    def excluir_instrutor(self):
        self.__lista_instrutores()
        cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
        instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

        if(instrutor is not None):
            self.__instrutores.remove(instrutor)
            self.lista_instrutores()
        else:
            self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Instrutor não existente")

    def lista_instrutores(self):
        if len(self.__instrutores) == 0:
            self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não existe instrutores")
        else:
            for instrutor in self.__instrutores:
                #Fazer tratamento de dados aqui ou em "mostra_instrutor"?
                self.__tela_instrutor.mostra_instrutor({"nome": instrutor.nome, "sexo": instrutor.sexo, "cpf": instrutor.cpf, "cref": instrutor.cref})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_instrutor, 2: self.alterar_instrutor, 3: self.lista_instrutores, 4: self.excluir_instrutor, 5: self.vincular_aluno, 6: self.desvincular_aluno, 7: self.lista_alunos_vinculados}

        while (True):
            lista_opcoes[self.__tela_instrutor.tela_opcoes()]()
