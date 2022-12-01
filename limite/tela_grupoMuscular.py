class TelaGrupoMuscular():

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO EXERCICIO - GRUPO MUSCULAR=============")
        print("1 - Incluir exercicio")
        print("2 - Remover exercicio")
        print("3 - Listar exercicios por grupo muscular")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao and opcao != 0:
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
        
    def seleciona_grupoMuscular(self):
        grupoMuscular = input("Digite o grupo muscular:")
        if isinstance(grupoMuscular, str):
            if (grupoMuscular == "Grupo Muscular Um" 
            or grupoMuscular == "Grupo Muscular Dois"
            or grupoMuscular == "Grupo Muscular Tres"
            or grupoMuscular == "Grupo Muscular Quatro"
            or grupoMuscular == "Grupo Muscular Cinco"
            ):
                return grupoMuscular
            else:
                raise ValueError(">>>Ocorreu uma exceção ValueError")
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")