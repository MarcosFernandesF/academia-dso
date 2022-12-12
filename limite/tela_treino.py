from entidade import exercicio


class TelaTreino():

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO TREINO =============")
        print("1 - Criar treino")
        print("2 - Alterar treino")
        print("3 - Remover treino")
        print("4 - Listar treinos")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4  and opcao != 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        if isinstance(id_exercicio, int):
            return str(id_exercicio)
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    def pega_dados_treino(self):
        print("=========== DADOS TREINO ===========")
        nome = input("Nome do treino: ")
        exercicio = input("ID do exercicio: ") 
        duracao = input("Duração do treino (em minutos): ")
        cref = input("CREF do instrutor: ")
        return {"nome": nome, "id_exercicio": str(exercicio), "duracao": int(duracao), "cref": str(cref)}
    
    def seleciona_treino(self):
        id_treino = input("Digite o ID do treino: ")
        print("")

        return str(id_treino)
