from tela import Tela

class TelaInstrutor(Tela):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("------------- INSTRUTOR -------------")
        print("Escolha uma opção:")
        print("1 - Incluir Instrutor")
        print("2 - Alterar Instrutor")
        print("3 - Listar Instrutores")
        print("4 - Excluir Instrutor")
        print("5 - Vincular Aluno")
        print("6 - Desvincular Aluno")
        print("7 - Listar Alunos Vinculados")

        opcao = int(input("Digite a opção: "))
        return opcao
    
    #Fazer o tratamento de dados aqui, caso a entrada seja diferente do esperado
    def pega_dados_instrutor(self):
        print("--------- DADOS INSTRUTOR ---------")
        nome = input("Nome: ")
        sexo = input("Sexo: ")
        cref = input("CREF: ")
        cpf = input("CPF: ")

        return {"nome": nome, "sexo": sexo, "cref": cref, "cpf": cpf}

    #Fazer o tratamento de dados aqui, caso a enrada seja diferente do esperado
    def mostra_instrutor(self, dados_instrutor):
        print("Nome do Instrutor: ", dados_instrutor["nome"])
        print("Sexo do Instrutor: ", dados_instrutor["sexo"])
        print("CREF do Instrutor: ", dados_instrutor["cref"])
        print("CPF do Instrutor: ", dados_instrutor["cpf"])
        print("\n")

    #Fazer o tratamento de dados aqui, caso a enrada seja diferente do esperado
    def seleciona_instrutor(self):
        cpf = input("CPF do instrutor que deseja selecionar: ")
        return cpf

    ##Metodos Abstratos
    def seleciona_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        return cpf
    