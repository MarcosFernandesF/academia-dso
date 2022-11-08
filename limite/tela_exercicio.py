from limite.tela import Tela

class TelaExercicio(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------ MENU EXERCICIOS ------------")
        print("1 - Incluir Exercício")
        print("2 - Alterar Exercício")
        print("3 - Listar Exercícios")
        print("4 - Excluir Exercício")
        print("0 - Voltar")

        opcao = int(input("Escolha a opção: "))
        print("")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

        return opcao
    
    #Fazer um id do aparelho automatico (que incrementa)
    #Excluir o inpuit dos dois ids apos arrumar.
    def pega_dados_exercicio(self):
        print("-------- DADOS EXERCICIO --------")
        nome = input("Nome: ")
        id = input("ID do Aparelho: ")
        id_exercicio = input("ID do Exercício: ")
        print("")

        if isinstance(nome, str):
            return {"nome": nome, "id": id, "id_exercicio": id_exercicio}
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    #Excluir o input do id apos arrumar
    def mostra_exercicio(self, dados_exercicio):
        print("Nome do Exercício: ", dados_exercicio["nome"])
        print("Aparelho utilizado no Exercício:", dados_exercicio["aparelho"])
        print("ID do Exercício: ", dados_exercicio["id_exercicio"])
        print("")           
    
    def seleciona_exercicio(self):
        #Mudar id para int no diagrama
        id_exercicio = input ("ID do Exercício: ")
        print("")

        if isinstance(id_exercicio, int):
            return id_exercicio
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
