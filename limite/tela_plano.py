from limite.tela import Tela

class TelaPlano(Tela):
    def __init__(self):
        super().__init__()

    def mostra_plano(self, dados_plano):
        print("Nome: ", dados_plano["nome"])
        print("Duracao: ", dados_plano["duracao"])
        print("Preço: ", dados_plano["preco"])
        print("Codigo: ", dados_plano["codigo"])
        print("")