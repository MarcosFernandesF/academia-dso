from limite.tela import Tela
from exception.menu_not_found_error import MenuNotFoundError

class TelaExercicio(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------ MENU EXERCICIOS ------------")
        print("1 - Criar exercício")
        print("2 - Modificar exercício")
        print("3 - Listar exercícios")
        print("4 - Excluir exercício")
        print("0 - Voltar")

        opcao = int(input("Escolha a opção: "))
        print("")

        if opcao > 4 or opcao < 0:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")

        return opcao
    
    def pega_dados_exercicio(self):
        print("-------- DADOS EXERCICIO --------")
        nome = input("Nome: ")
        id = input("ID do Aparelho: ")
        print("")

        if isinstance(nome, str):
            return {"nome": nome, "id_aparelho": id}
    
    def mostra_exercicio(self, dados_exercicio):
        print("Nome do Exercício: ", dados_exercicio["nome"])
        print("ID do aparelho:", dados_exercicio["aparelho"])
        print("ID do exercício: ", dados_exercicio["id_exercicio"])
        print("")           
    
    def seleciona_exercicio(self):
        id_exercicio = int(input("ID do Exercício: "))
        print("")

        if isinstance(id_exercicio, int):
            return str(id_exercicio)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    
