from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno
from DAOs.aluno_dao import AlunoDAO
from exception.menu_not_found_error import MenuNotFoundError
from exception.cpf_not_found_error import CpfNotFoundError

class ControladorAluno():
    
    def __init__(self, controlador_sistema):
        #self.__alunos = []
        self.__aluno_DAO = AlunoDAO() #Lista de alunos

        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    @property
    def tela_aluno(self):
        return self.__tela_aluno

    def verifica_plano(self, lista_de_planos: list, dados_aluno: dict):
        for plano in lista_de_planos.get_all():
            if plano.nome == dados_aluno["plano"]:
                return plano

        return None

    def pega_aluno_por_cpf(self, cpf: str):
        for aluno in self.__aluno_DAO.get_all():
            if(aluno.cpf == cpf):
                return aluno
        else:
            raise CpfNotFoundError(">>>Ocorreu uma exceção CpfNotFoundError")

    def incluir_aluno(self):
        try:
            lista_de_planos = self.__controlador_sistema.controlador_plano.plano_DAO

            dados_aluno = self.__tela_aluno.pega_dados_aluno()

            dados_aluno["plano"] = self.verifica_plano(lista_de_planos, dados_aluno)

            if dados_aluno["plano"] is None:
                raise ValueError("Nenhum plano com este nome foi encontrado")

            for aluno in self.__aluno_DAO.get_all():
                if dados_aluno["cpf"] == aluno.cpf:
                    self.__tela_aluno.mostra_mensagem("Já existe um aluno com este CPF!\n")
                    break
            else:
                aluno = Aluno(dados_aluno["nome"], dados_aluno["sexo"], dados_aluno["cpf"], dados_aluno["plano"])
                #self.__alunos.append(aluno)
                self.__aluno_DAO.add(aluno)
                self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso!\n")

        except TypeError as e:
            self.__tela_aluno.mostra_mensagem(e)
            self.__tela_aluno.mostra_mensagem(">>>Alguma das entradas estão com o tipo diferente do que deveriam estar!")          
            self.__tela_aluno.mostra_mensagem(">>>nome[str], sexo[str], cpf[str]\n")
        except ValueError as e:
            self.__tela_aluno.mostra_mensagem(e)
            self.__tela_aluno.mostra_mensagem(">>>A entrada 'Sexo' ou o 'Plano' foram escritos de maneira errada!")          
            self.__tela_aluno.mostra_mensagem(">>>Verificar a lista de planos!")
            self.__tela_aluno.mostra_mensagem(">>>Maneira Correta: Masculino / Feminino")
        except CpfNotFoundError as e:
            self.__tela_aluno.mostra_mensagem(e)
            

    def alterar_aluno(self):
        try:
            if (self.lista_alunos()) is not None:
                cpf_aluno = self.__tela_aluno.seleciona_aluno()
                aluno = self.pega_aluno_por_cpf(cpf_aluno)

                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
                lista_de_planos = self.__controlador_sistema.controlador_plano.plano_DAO

                novos_dados_aluno["plano"] = self.verifica_plano(lista_de_planos, novos_dados_aluno)

                for aluno in self.__aluno_DAO.get_all():
                    if novos_dados_aluno["cpf"] == aluno.cpf:
                        self.__tela_aluno.mostra_mensagem("Já existe um aluno com este CPF!\n")
                        break
                else:
                    aluno.nome = novos_dados_aluno["nome"]
                    aluno.sexo = novos_dados_aluno["sexo"]
                    aluno.cpf = novos_dados_aluno["cpf"]
                    aluno.plano = novos_dados_aluno["plano"]
                    self.__aluno_DAO.update(cpf_aluno, aluno)

        except ValueError as e:
            self.__tela_aluno.mostra_mensagem(e)
            self.__tela_aluno.mostra_mensagem(">>>Entrada Inválida para o sexo!")          
            self.__tela_aluno.mostra_mensagem(">>>Maneira correta: Masculino / Feminino\n")
        except TypeError as e:
            self.__tela_aluno.mostra_mensagem(e)
            self.__tela_aluno.mostra_mensagem(">>>O plano digitado é nulo")
        except CpfNotFoundError as e:
            self.__tela_aluno.mostra_mensagem(e)

    def excluir_aluno(self):
        try:
            if (self.lista_alunos()) is not None:
                cpf_aluno = self.__tela_aluno.seleciona_aluno()
                aluno = self.pega_aluno_por_cpf(cpf_aluno)

                self.__aluno_DAO.remove(aluno.cpf)
                self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso! \n")

        except CpfNotFoundError as e:
            self.__tela_aluno.mostra_mensagem(e)

    def lista_alunos(self):
        if len(self.__aluno_DAO.get_all()) == 0:
            self.__tela_aluno.mostra_mensagem("ATENÇÃO: Não existe alunos cadastrados\n")
            return None
        else:
            self.__tela_aluno.mostra_mensagem("---------- LISTA DE ALUNOS ----------")
            for aluno in self.__aluno_DAO.get_all():
                #Não fiz o tratamento aqui pois se estivesse errado ele não passario do "pega_dados_aluno"
                self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "sexo": aluno.sexo, "cpf": aluno.cpf, "plano": aluno.plano})
            return True

    def retornar(self):
        self.__controlador_sistema.abre_tela_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.lista_alunos, 4: self.excluir_aluno, 0: self.retornar}

        while (True):
            try:
                lista_opcoes[self.__tela_aluno.tela_opcoes()]()
            except MenuNotFoundError as e:
                self.__tela_aluno.mostra_mensagem(e)
