from limite.tela import Tela
from exception.menu_not_found_error import MenuNotFoundError

class TelaPlano(Tela):
    
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------- PLANO -------------")
        print("Escolha uma opção:")
        print("1 - Incluir Plano")
        print("2 - Alterar Plano")
        print("3 - Listar Planos")
        print("4 - Excluir Plano")
        print("0 - Voltar")

        opcao = int(input("Digite a opção: "))
        print("")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")

        return opcao

    def pega_dados_plano(self):
        print("--------- DADOS PLANO ---------")
        nome = input("Nome: ")
        duracao = input("Duração - Mensal, Semestral ou Anual: ")
        preco = float(input("Preço: "))
        print("")

        if isinstance(nome, str) and isinstance(duracao, str) and isinstance(preco, float) and nome is not None and duracao is not None and preco is not None:
            if duracao == "Mensal" or duracao == "Semestral" or duracao == "Anual":
                return {"nome": nome, "duracao": duracao, "preco": preco}
            else:
                raise ValueError(">>>Ocorreu uma exceção ValueError")
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    def seleciona_plano(self):
        nome = input("Digite o nome do plano que deseja selecionar: ")
        print("")

        if isinstance(nome, str) and nome is not None:
            return nome
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")  

    def mostra_plano(self, dados_plano):
        print("Nome: ", dados_plano["nome"])
        print("Duracao: ", dados_plano["duracao"])
        print("Preço: ", dados_plano["preco"])
        print("")