from limite.tela import Tela
from exception.menu_not_found_error import MenuNotFoundError

class TelaSistema(Tela):

    def __init__(self):
        super().__init__()

    def mostra_tela_opcoes(self):
        print("\n<---------- MENU PRINCIPAL --------- >")
        print("Escolha sua opção:")
        print("1 - Aluno")
        print("2 - Instrutor")
        print("3 - Grupo Muscular")
        print("4 - Planos")
        print("5 - Aparelho")
        print("6 - Exercicio")
        print("7 - Treino")
        print("0 - Encerra Programa")
        opcao = int(input("Escolha a opção: "))
        print("")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7 and opcao != 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")

        return opcao