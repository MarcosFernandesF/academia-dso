class TelaSistema:

    def mostra_tela_opcoes(self):
        print("<---------- MENU PRINCIPAL --------- >")
        print("Escolha sua opção:")
        print("1 - Aluno")
        print("2 - Instrutor")
        print("3 - Grupo Muscular")
        print("4 - Plano")
        print("5 - Aparelho")
        print("6 - Exercicio")
        print("7 - Treino")
        opcao = int(input("Escolha a opção: "))
        return opcao