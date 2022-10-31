from limite.tela import Tela

class TelaAluno(Tela):
    
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------- ALUNO -------------")
        print("Escolha uma opção:")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Aluno")
        print("4 - Excluir Aluno")
        print("0 - Voltar")

        opcao = int(input("Digite a opção: "))
        print("")
        return opcao

    def mostra_aluno(self, dados_aluno):
        print("Nome do aluno: ",dados_aluno["nome"])
        print("Sexo: ",dados_aluno["sexo"])
        print("CPF: ",dados_aluno["cpf"])
        print("Plano: ",dados_aluno["plano"].nome)
        print("")

    #Fazer o tratamento de dados aqui, caso a entrada seja diferente do esperado
    def pega_dados_aluno(self):
        print("--------- DADOS ALUNO ---------")
        nome = input("Nome: ")
        sexo = input("Sexo[Masculino/Feminino]: ")
        cpf = input("CPF: ")
        plano = input("Plano[Mensal, Semestral, Anual]: ")
        print("")

        if sexo == "Masculino" or sexo == "Feminino" or plano == "Mensal" or plano == "Semestral" or plano == "Anual":
            return {"nome": nome, "sexo": sexo, "cpf": cpf, "plano": plano}
        else:
            raise ...
        