from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, turma, turno):
        super().__init__(nome, cpf)
        self.__turma = turma
        self.__turno = turno

    @property
    def turma(self):
        return self.__turma

    @property
    def turno(self):
        return self.__turno

    def __str__(self):
        return "ALUNO: "+super().nome+" | CPF: "+super().cpf+\
               " | Turma: "+self.__turma+" | Turno: "+self.__turno