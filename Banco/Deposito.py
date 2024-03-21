from Transacao import Transacao


class Deposito(Transacao):

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):

        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)