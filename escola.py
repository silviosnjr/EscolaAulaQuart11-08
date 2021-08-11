from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

class Escola():
    def __init__(self):
        self.__nome = "Escola Estadual dos Programadores do Futuro"

        aluno1 = Aluno("Ciclano de Tal", "111.222.333-44", "222-333-44", "noite")
        aluno2 = Aluno("Maria de Souza", "333.222.333-44", "000-333-44", "tarde")
        professor1 = Professor("Beltrano de Tal", "000.000.111-11", "Geografia", "concursado")
        funcionario1 = Funcionario("Fulano da Silva", "111.000.111-11", "Zelador", "08 as 12h")

        self.__pessoas = [aluno1, aluno2, professor1, funcionario1]

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitarAcesso(self):
        codigo_acesso = input("Qual o seu código de acesso: ")
        for pessoa in self.__pessoas:
            if (pessoa.acessarEscola(codigo_acesso)):
                return True
        print("Acesso negado!")
        return False