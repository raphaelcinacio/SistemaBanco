from Cliente import Cliente


class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf

    def __str__(self):
        return str(
            {
                "cpf": self.cpf,
                "nome": self.__nome
            }
        )