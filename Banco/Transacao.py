from abc import ABC, abstractmethod


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @property
    @abstractmethod
    def registrar(self, conta):
        pass