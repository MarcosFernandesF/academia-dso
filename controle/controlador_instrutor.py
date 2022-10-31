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
    
    def pega_instrutor_por_cref(self, cref: str):
        for instrutor in self.__instrutores:
            if(instrutor.cref == cref):
                return instrutor
        return None

    #Fazer tratamento dos dados no "pega_dados_instrutor"
    def incluir_instrutor(self):
        dados_instrutor = self.__tela_instrutor.pega_dados_instrutor()
        instrutor = Instrutor(dados_instrutor["nome"], dados_instrutor["sexo"], dados_instrutor["cpf"], dados_instrutor["cref"])
        self.__instrutores.append(instrutor)

    def alterar_instrutor(self):
        if (self.lista_instrutores()) is not None:
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
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há instrutor com este CPF!\n")

    def excluir_instrutor(self):
        if (self.lista_instrutores()) is not None:
            cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
            instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

            if(instrutor is not None):
                self.__instrutores.remove(instrutor)
                self.lista_instrutores()
            else:
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há instrutor com este CPF!\n")

    def lista_instrutores(self):
        if len(self.__instrutores) == 0:
            self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não existe instrutores\n")
            return None
        else:
            self.__tela_instrutor.mostra_mensagem("---------- LISTA DE INSTRUTORES ----------")
            for instrutor in self.__instrutores:
                #Fazer tratamento de dados aqui ou em "mostra_instrutor"?
                self.__tela_instrutor.mostra_instrutor({"nome": instrutor.nome, "sexo": instrutor.sexo, "cpf": instrutor.cpf, "cref": instrutor.cref})
            return True

    def vincular_aluno(self):
        controlador_aluno = self.__controlador_sistema.controlador_aluno

        if (self.lista_instrutores()) is not None:
            self.__tela_instrutor.mostra_mensagem("Para qual instrutor deseja vincular um aluno?\n")

            cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
            instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

            if (instrutor is not None):
                self.__tela_instrutor.mostra_mensagem("Qual aluno deseja vincular? \n")
                controlador_aluno.lista_alunos()

                cpf_aluno = self.__tela_instrutor.seleciona_aluno()
                aluno = controlador_aluno.pega_aluno_por_cpf(cpf_aluno)

                if(aluno is None):
                    self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há aluno com este CPF!\n")
                else:
                    instrutor.alunos = aluno
                    self.__tela_instrutor.mostra_mensagem("Aluno vinculado com sucesso!\n")
            else:
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há instrutor com este CPF!\n")

    def desvincular_aluno(self):
        controlador_aluno = self.__controlador_sistema.controlador_aluno

        if (self.lista_instrutores()) is not None:
            self.__tela_instrutor.mostra_mensagem("Para qual instrutor deseja desvincular um aluno?\n")

            cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
            instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

            if (instrutor is not None):
                self.__tela_instrutor.mostra_mensagem("Qual aluno deseja desvincular? \n")
                controlador_aluno.lista_alunos()
                cpf_aluno = self.__tela_instrutor.seleciona_aluno()
                aluno = controlador_aluno.pega_aluno_por_cpf(cpf_aluno)
                if(aluno is None):
                    self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há aluno com este CPF!\n")
                else:
                    instrutor.alunos.remove(aluno)
                    self.__tela_instrutor.mostra_mensagem("Aluno desvinculado com sucesso!\n")
            else:
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não há instrutor com este CPF!\n")

    def lista_alunos_vinculados(self):
        if (self.lista_instrutores()) is not None:
            cpf_instrutor = self.__tela_instrutor.seleciona_aluno()
            instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

            if len(instrutor.alunos) == 0:
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não existe alunos vinculados!\n")
            else:
                self.__tela_instrutor.mostra_mensagem("---------- LISTA DE ALUNOS VINCULADOS ----------")
                for aluno in instrutor.alunos:
                    self.__controlador_sistema.controlador_aluno.tela_aluno.mostra_aluno({"nome": aluno.nome, "sexo": aluno.sexo, "cpf": aluno.cpf, "plano": aluno.plano})


    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_instrutor, 2: self.alterar_instrutor, 3: self.lista_instrutores, 4: self.excluir_instrutor, 5: self.vincular_aluno, 6: self.desvincular_aluno, 7: self.lista_alunos_vinculados, 0: self.retornar}

        while (True):
            lista_opcoes[self.__tela_instrutor.tela_opcoes()]()
