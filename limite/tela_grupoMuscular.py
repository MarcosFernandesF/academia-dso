class TelaGrupoMuscular():

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO EXERCICIO - GRUPO MUSCULAR=============")
        print("1 - Incluir exercicio")
        print("2 - Remover exercicio")
        print("3 - Listar exercicios por grupo muscular")
        print("0 - Voltar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def mostra_opcoes_grupo_muscular(self):
        print("<-------- ESCOLHA O GRUPO MUSCULAR ------>")
        print("1 - Grupo Muscular Um")
        print("2 - Grupo Muscular Um")
        print("3 - Grupo Muscular Um")
        print("4 - Grupo Muscular Um")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        return id_exercicio