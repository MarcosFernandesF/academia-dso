from exception.menu_not_found_error import MenuNotFoundError
from limite.tela import Tela

class TelaGrupoMuscular(Tela):

    def __init__(self):
        super().__init__()

    def mostra_tela_opcoes(self):
        print("=========== CADASTRO EXERCICIO - GRUPO MUSCULAR=============")
        print("1 - Incluir exercicio")
        print("2 - Remover exercicio")
        print("3 - Listar exercicios por grupo muscular")
        print("4 - Criar grupo muscular")
        print("5 - Listar grupos")
        print("6 - Modificar grupo muscular")
        print("7 - Excluir grupo muscular")
        print("0 - Voltar")
        opcao = int(input("Escolha a opção: "))

        if opcao < 0 or opcao > 7:
            raise MenuNotFoundError(">>>Ocorreu uma exceção MenuNotFoundError")
        return opcao

    def seleciona_exercicio(self):
        id_exercicio = input ("ID do Exercício: ")
        if isinstance(id_exercicio, int):
            return id_exercicio
        return None

    def pega_id_grupo_muscular(self):
        id = input("Digite o ID do grupo muscular: ")
        return str(id)

    def pega_dados_grupo_muscular(self):
        print("-------- DADOS GRUPO MUSCULAR --------")
        nome = input("Nome: ")
        print("")

        if isinstance(nome, str):
            return {"Nome": nome}
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")
    
    def mostra_grupo_muscular(self, grupo):
        print(f"Nome: {grupo.nome} | ID: {grupo.id}")
    