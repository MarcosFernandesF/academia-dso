class TelaExercicio():

    def mostra_tela_opcoes(self):
        print("\n<--------- MENU EXERCICIOS --------->")
        print("1 - Registrar exercício")
        print("2 - Modificar exercício")
        print("3 - Excluir exercício")
        print("4 - Listar exercícios")
        print("0 - Sair")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_dados_exercicio(self):
        print("\n<-------- DADOS EXERCICIO ------->")
        nome = input("Nome: ")
        id = input("ID do aparelho: ")
        id_exercicio = input("ID do Exercício: ")
        return {"nome": nome, "id": id, "id_exercicio": id_exercicio}
    
    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        return id_exercicio
    
    def mostra_exercicio(self, dados_exercicio):
        print("\nNome do exercício: ", dados_exercicio["nome"])
        print("Aparelho utilizado no exercício:", dados_exercicio["aparelho"])
        print("ID do exercício: ", dados_exercicio["id_exercicio"])
        print("\n")