from Conta import Conta


class ContaCorrente(Conta):

    def __init__(self, cliente, numero_conta, limite=500, limite_saques=3):
        super().__init__(cliente, numero_conta)
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta_corrente(cls, cliente, numero_conta, limite=500, limite_saques=3):
        return ContaCorrente(cliente, numero_conta, limite, limite_saques)

    def sacar(self, valor):

        if valor > self.saldo or self.limite_saques == 0:
            print("Não foi possível efetuar o saque")
            return False
        else:
            self.limite_saques -= 1
            return super().sacar(valor)

    def depositar(self, valor):
        if valor > 0:
            return super().depositar(valor)
        else:
            print("Não foi possível depositar")
            return False

    def to_dict(self):
        return {
            "cliente": self.cliente,
            "numero_conta": self.numero
        }
