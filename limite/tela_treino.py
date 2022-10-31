from entidade import exercicio


class TelaTreino():

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO TREINO =============")
        print("1 - Criar treino")
        print("2 - Alterar treino")
        print("3 - Remover treino")
        print("3 - Listar treinos")
        print("0 - Voltar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        return id_exercicio

    def pega_dados_treino(self):
        print("=========== DADOS TREINO ===========")
        nome = input("Nome do treino: ")
        exercicio = input("ID do exercicio: ") 
        duracao = input("Duração do treino (em minutos): ")
        cref = input("CREF do instrutor: ")
        id_treino = input("Digite o id do treino:")
        return {"nome": nome, "id_exercicio": exercicio, "duracao": duracao, "cref": cref, "id_treino": id_treino}
