from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, formacao, vinculo):
        super().__init__(nome, cpf)
        self.__formacao = formacao
        self.__vinculo = vinculo

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__vinculo

    def __str__(self):
        return "PROFESSOR: "+super().nome+" | CPF: "+super().cpf+" | Formação: "+self.__formacao+" | Vínculo: "+self.__vinculo