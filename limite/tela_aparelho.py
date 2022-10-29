class TelaAparelho():

    def mostra_tela_opcoes(self):
        print("\n<--------- MENU APARELHOS --------->")
        print("1 - Listar aparelhos")
        print("0 - Voltar")

        opcao = int(input("Escolha a opção: "))
        return opcao