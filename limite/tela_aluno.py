from limite.tela import Tela
from exception.menu_not_found_error import MenuNotFoundError

class TelaAluno(Tela):
    
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------- ALUNO -------------")
        print("Escolha uma opção:")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Aluno")
        print("4 - Excluir Aluno")
        print("0 - Voltar")

        opcao = int(input("Digite a opção: "))
        print("")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")
            
        return opcao

    def mostra_aluno(self, dados_aluno):
        print("Nome do aluno: ",dados_aluno["nome"])
        print("Sexo: ",dados_aluno["sexo"])
        print("CPF: ",dados_aluno["cpf"])
        print("Plano: ",dados_aluno["plano"].nome)
        print("")

    def pega_dados_aluno(self):
        print("--------- DADOS ALUNO ---------")
        nome = input("Nome: ")
        sexo = input("Sexo[Masculino/Feminino]: ")
        cpf = input("CPF: ")
        plano = input("Plano: ")
        print("")

        if isinstance(nome, str) and isinstance(sexo, str) and isinstance(cpf, str):
            if (sexo == "Masculino" or sexo == "Feminino"):
                return {"nome": nome, "sexo": sexo, "cpf": cpf, "plano": plano}
            else:
                raise ValueError(">>>Ocorreu uma exceção ValueError")
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
        
    def seleciona_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        print("")

        if isinstance(cpf, str):
            return cpf
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")