class TelaGrupoMuscular():

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO EXERCICIO - GRUPO MUSCULAR=============")
        print("1 - Incluir exercicio")
        print("2 - Remover exercicio")
        print("3 - Listar exercicios por grupo muscular")
        print("4 - Criar grupo muscular")
        print("5 - Listar grupos")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))

        if opcao < 0 or opcao > 5:
            raise ValueError(">>>Ocorreu uma exceção ValueError")
        return opcao
    
    def mostra_opcoes_grupo_muscular(self):
        print("<-------- ESCOLHA O GRUPO MUSCULAR ------>")
        print("1 - Grupo Muscular Um")
        print("2 - Grupo Muscular Dois")
        print("3 - Grupo Muscular Tres")
        print("4 - Grupo Muscular Quatro")
        print("5 - Grupo Muscular Cinco")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao and opcao != 4 and opcao != 5 and opcao != 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        if isinstance(id_exercicio, int):
            return id_exercicio
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
        
    def pega_id_grupo_muscular(self):
        id = input("Digite o id do grupo muscular:")
        if isinstance(id, int):
            return id
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
        
    def pega_dados_grupo_muscular(self):
        print("-------- DADOS GRUPO MUSCULAR --------")
        nome = input("Nome: ")
        print("")

        if isinstance(nome, str):
            return nome
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    def mostra_grupo_muscular(self, grupo):
        print(f"Nome: {grupo.nome} | ID: {grupo.id}")
    