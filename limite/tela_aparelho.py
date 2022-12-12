from exception.menu_not_found_error import MenuNotFoundError
from limite.tela import Tela

class TelaAparelho(Tela):

    def __init__(self):
        super().__init__()

    def mostra_tela_opcoes(self):
        print("\n<--------- MENU APARELHOS --------->")
        print("1 - Listar aparelhos")
        print("0 - Voltar") 
        opcao = int(input("Escolha a opção: "))

        if opcao != 1 and opcao != 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")  
        return opcao