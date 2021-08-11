class PessoaFisica :
    def __init__(self, name, cpf):
        self.__nome = name
        self.__cpf = cpf

    @property
    def nome(self) :
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf