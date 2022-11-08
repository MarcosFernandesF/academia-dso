from limite.tela import Tela

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
        print("0 - Voltar")

        opcao = int(input("Digite a opção: "))
        print("")

        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 7 and opcao != 0:
            raise ValueError(">>>Ocorreu uma exceção ValueError")

        return opcao
    
    #Fazer o tratamento de dados aqui, caso a entrada seja diferente do esperado
    def pega_dados_instrutor(self):
        print("--------- DADOS INSTRUTOR ---------")
        nome = input("Nome: ")
        sexo = input("Sexo[Masculino/Feminino]: ")
        cref = input("CREF: ")
        cpf = input("CPF: ")
        print("")

        if isinstance(nome, str) and isinstance(sexo, str) and isinstance(cref, str) and isinstance(cpf, str):
            if sexo == "Masculino" or sexo == "Feminino":
                return {"nome": nome, "sexo": sexo, "cref": cref, "cpf": cpf}
            else:
                raise ValueError(">>>Ocorreu uma exceção ValueError")
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")

    def mostra_instrutor(self, dados_instrutor):
        print("Nome do Instrutor: ", dados_instrutor["nome"])
        print("Sexo do Instrutor: ", dados_instrutor["sexo"])
        print("CREF do Instrutor: ", dados_instrutor["cref"])
        print("CPF do Instrutor: ", dados_instrutor["cpf"])
        print("")

    #Fazer o tratamento de dados aqui, caso a enrada seja diferente do esperado
    #Implementar validação cpf
    def seleciona_instrutor(self):
        cpf = input("CPF do instrutor que deseja selecionar: ")
        print("")

        if isinstance(cpf, str):
            return cpf
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")  
            
    ##Metodos Abstratos
    def seleciona_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        print("")

        if isinstance(cpf, str):
            return cpf
        else:
            raise TypeError(">>>Ocorreu uma exceção TypeError")