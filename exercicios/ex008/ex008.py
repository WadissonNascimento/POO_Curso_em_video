from rich import print, inspect
class ContaBancaria:
    """
Cria uma conta bancaria que pode realizar saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id #público
        self._titular = nome #protegido 
        self.__saldo = saldo #private

    def __str__(self):
        #return f"A conta {self.id} pertence ao titular {self.titular} e está com o saldo de R${self.saldo:.2f}"
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado seu novo saldo é de R${self.__saldo:.2f}")

    def sacar(self, valor):
        valor = abs(valor)
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado seu novo saldo é de R${self.__saldo:.2f}")
        else:
            print("Saldo insuficiente.")

