class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.__contas = []

    @property
    def contas(self):
        return self.__contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def __str__(self):
        return str(
            {
                "endereco": self.endereco
            }
        )



