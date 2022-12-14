from entidade import exercicio
from exception.menu_not_found_error import MenuNotFoundError
from limite.tela import Tela

class TelaTreino(Tela):

    def __init__(self):
        super().__init__()

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO TREINO =============")
        print("1 - Criar treino")
        print("2 - Alterar treino")
        print("3 - Remover treino")
        print("4 - Listar treinos")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        if isinstance(id_exercicio, int):
            return str(id_exercicio)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    def pega_dados_treino(self):
        print("=========== DADOS TREINO ===========")
        nome = input("Nome do treino: ")
        exercicio = input("ID do exercicio: ") 
        duracao = input("Duração do treino (em minutos): ")
        cref = input("CREF do instrutor: ")
        print("")

        if isinstance(nome, str) and isinstance(exercicio, str) and isinstance(duracao, str) and isinstance(cref, str):
            return {"nome": nome, "id_exercicio": str(exercicio), "duracao": int(duracao), "cref": str(cref)}
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    def seleciona_treino(self):
        id_treino = input("Digite o ID do treino: ")
        print("")

        return str(id_treino)
