import self as self


class conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    @property
    def nome(self):
        return self._titular

    @property
    def numero(self):
        return self._numero

    @property
    def extrato(self):
        return self._saldo

    def set_depositar(self, valor):
        self._saldo += valor

    def set_sacar(self, valor):
        self._saldo -= valor

    def set_tranferir(self, valor, destino):
        self.set_sacar(valor)
        destino.set_depositar(valor)









