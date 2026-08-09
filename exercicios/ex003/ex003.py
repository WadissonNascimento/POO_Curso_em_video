from rich import print, inspect
class ContaBancaria:
    """
Cria uma conta bancaria que pode realizar saques e depósitos.
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} pertence ao titular {self.titular} e está com o saldo de R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado seu novo saldo é de R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado seu novo saldo é de R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

c = ContaBancaria(112, "José", 500)

inspect(c)