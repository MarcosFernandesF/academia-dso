
class MenuNotFoundError(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem + "\n>>>A opção de menu digitada não existe!\n")
