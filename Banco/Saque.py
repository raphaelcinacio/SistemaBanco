from Transacao import Transacao


class Saque(Transacao):

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)
