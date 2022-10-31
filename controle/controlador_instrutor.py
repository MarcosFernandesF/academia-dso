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
        else:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

    def incluir_instrutor(self):
        try:
            dados_instrutor = self.__tela_instrutor.pega_dados_instrutor()
            for instrutor in self.__instrutores:
                if dados_instrutor["cpf"] == instrutor.cpf:
                    self.__tela_instrutor.mostra_mensagem("Já existe um instrutor com este CPF!\n")
                    break
            else:
                instrutor = Instrutor(dados_instrutor["nome"], dados_instrutor["sexo"], dados_instrutor["cpf"], dados_instrutor["cref"])
                self.__instrutores.append(instrutor)
                
        except TypeError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Alguma das entradas estão com o tipo diferente do que deveriam estar!")          
            self.__tela_instrutor.mostra_mensagem(">>>nome[str], sexo[str], cref[float], cpf[int]\n")
        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>A entrada 'Sexo' foi escrita de maneira errada!")          
            self.__tela_instrutor.mostra_mensagem(">>>Maneira certa: Masculino / Feminino\n")

    def alterar_instrutor(self):
        try:
            if (self.lista_instrutores()) is not None:
                cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
                instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

                novos_dados_instrutor = self.__tela_instrutor.pega_dados_instrutor()
                instrutor.nome = novos_dados_instrutor["nome"]
                instrutor.sexo = novos_dados_instrutor["sexo"]
                instrutor.cpf = novos_dados_instrutor["cpf"]
                instrutor.cref = novos_dados_instrutor["cref"]

        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Entrada Inválida!")          
            self.__tela_instrutor.mostra_mensagem(">>>Escreva a entrada de maneira correta!\n")

    def excluir_instrutor(self):
        try:
            if (self.lista_instrutores()) is not None:
                cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
                instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

                self.__instrutores.remove(instrutor)
                self.lista_instrutores()

        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Não há nenhum instrutor com este CPF!\n") 

    def lista_instrutores(self):
        if len(self.__instrutores) == 0:
                self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não existe instrutores\n")
                return None
        else:
            self.__tela_instrutor.mostra_mensagem("---------- LISTA DE INSTRUTORES ----------")
            for instrutor in self.__instrutores:
                #Não fiz o tratamento aqui pois se estivesse errado ele não passario do "pega_dados_instrutor"
                self.__tela_instrutor.mostra_instrutor({"nome": instrutor.nome, "sexo": instrutor.sexo, "cpf": instrutor.cpf, "cref": instrutor.cref})
            return True

    def vincular_aluno(self):
        try:
            controlador_aluno = self.__controlador_sistema.controlador_aluno

            if (self.lista_instrutores()) is not None:
                self.__tela_instrutor.mostra_mensagem("Para qual instrutor deseja vincular um aluno?\n")

                cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
                instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

                self.__tela_instrutor.mostra_mensagem("Qual aluno deseja vincular? \n")
                controlador_aluno.lista_alunos()

                cpf_aluno = self.__tela_instrutor.seleciona_aluno()
                aluno = controlador_aluno.pega_aluno_por_cpf(cpf_aluno)

                for aluno in instrutor.alunos:
                    if cpf_aluno == aluno.cpf:
                        self.__tela_instrutor.mostra_mensagem("Esse aluno ja está vinculado ao instrutor!\n")
                        break
                else:
                    instrutor.alunos = aluno
                    self.__tela_instrutor.mostra_mensagem("Aluno vinculado com sucesso!\n")

        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Instrutor ou Aluno com CPF inválido!\n")

    def desvincular_aluno(self):
        try:
            controlador_aluno = self.__controlador_sistema.controlador_aluno

            if (self.lista_instrutores()) is not None:
                self.__tela_instrutor.mostra_mensagem("Para qual instrutor deseja desvincular um aluno?\n")
                
                cpf_instrutor = self.__tela_instrutor.seleciona_instrutor()
                instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

                controlador_aluno.lista_alunos()
                self.__tela_instrutor.mostra_mensagem("Qual aluno deseja desvincular? \n")

                cpf_aluno = self.__tela_instrutor.seleciona_aluno()
                aluno = controlador_aluno.pega_aluno_por_cpf(cpf_aluno)

                instrutor.alunos.remove(aluno)
                self.__tela_instrutor.mostra_mensagem("Aluno desvinculado com sucesso!\n")

        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Instrutor ou Aluno com CPF inválido!\n")

    def lista_alunos_vinculados(self):
        try:
            if (self.lista_instrutores()) is not None:
                cpf_instrutor = self.__tela_instrutor.seleciona_aluno()
                instrutor = self.pega_instrutor_por_cpf(cpf_instrutor)

                if len(instrutor.alunos) == 0:
                    self.__tela_instrutor.mostra_mensagem("ATENÇÃO: Não existe alunos vinculados!\n")
                else:
                    self.__tela_instrutor.mostra_mensagem("---------- LISTA DE ALUNOS VINCULADOS ----------")
                    for aluno in instrutor.alunos:
                        self.__controlador_sistema.controlador_aluno.tela_aluno.mostra_aluno({"nome": aluno.nome, "sexo": aluno.sexo, "cpf": aluno.cpf, "plano": aluno.plano})
        except ValueError as e:
            self.__tela_instrutor.mostra_mensagem(e)
            self.__tela_instrutor.mostra_mensagem(">>>Instrutor ou Aluno com CPF inválido!\n")


    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_instrutor, 2: self.alterar_instrutor, 3: self.lista_instrutores, 4: self.excluir_instrutor, 5: self.vincular_aluno, 6: self.desvincular_aluno, 7: self.lista_alunos_vinculados, 0: self.retornar}

        while (True):
            try:
                lista_opcoes[self.__tela_instrutor.tela_opcoes()]()
            except ValueError as e:
                self.__tela_instrutor.mostra_mensagem(e)
                self.__tela_instrutor.mostra_mensagem(">>>O valor digitado não corresponde as opções\n")
