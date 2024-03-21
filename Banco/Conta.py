from Historico import Historico


class Conta:

    numero_agencia = "0001"

    def __init__(self, cliente, numero_conta):
        self.__saldo = 0
        self.__numero = numero_conta
        self.__agencia = self.numero_agencia
        self.__cliente = cliente
        self.__historico = Historico()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def historico(self):
        return self.__historico

    @property
    def cliente(self):
        return self.__cliente

    @classmethod
    def nova_conta(cls, cliente):
        return Conta(cliente)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.__saldo -= valor
            print("Saque realizado com sucesso")
            return True
        else:
            print("Valor insuficiente")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Deposito realizado com sucesso")
            return True
        else:
            print("Valor inválido")
            return False


