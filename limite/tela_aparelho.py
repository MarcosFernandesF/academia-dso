from limite.tela import Tela


class TelaAparelho(Tela):

    def __init__(self):
        super().__init__()

    def mostra_tela_opcoes(self):
        print("\n<--------- MENU APARELHOS --------->")
        print("1 - Listar aparelhos")
        print("2 - Criar aparelho")
        print("3 - Modificar aparelho")
        print("4 - Excluir aparelho")
        print("0 - Voltar") 
        opcao = int(input("Escolha a opção: "))

        if opcao < 0 or opcao > 4:
            raise ValueError(">>>Ocorreu uma exceção ValueError")
        return opcao 
    
    def pega_dados_aparelho(self):
        print("\n-------- DADOS APARELHO --------")
        nome = input("Nome do aparelho: ")
        print("")

        if isinstance(nome, str):
            return {"Nome": nome}
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    def pega_id_aparelho(self):
        id = input("Digite o ID do aparelho: ")
        return str(id)