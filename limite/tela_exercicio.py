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

        if opcao > 4 or opcao < 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

        return opcao
    
    #Fazer um id do aparelho automatico (que incrementa)
    #Excluir o input do id aparelho.
    def pega_dados_exercicio(self):
        print("-------- DADOS EXERCICIO --------")
        nome = input("Nome: ")
        id = input("ID do Aparelho: ")
        print("")

        if isinstance(nome, str):
            return {"nome": nome, "id": id}
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    def mostra_exercicio(self, dados_exercicio):
        print("Nome do Exercício: ", dados_exercicio["nome"])
        print("Aparelho utilizado no Exercício:", dados_exercicio["aparelho"])
        print("ID do exercício: ", dados_exercicio["id_exercicio"])
        print("")           
    
    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        print("")

        if isinstance(id_exercicio, int):
            return id_exercicio
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
