class TelaAparelho():

    def mostra_tela_opcoes(self):
        print("\n<--------- MENU APARELHOS --------->")
        print("1 - Listar aparelhos")
        print("0 - Voltar") 
        opcao = int(input("Escolha a opção: "))

        if opcao != 1 and opcao != 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")  
        return opcao