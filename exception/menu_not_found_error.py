
class MenuNotFoundError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem + "\n>>>Não há registro com este cpf!\n")