from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
ph = PasswordHasher()

class ContaBancaria:
    def __init__(self, id, nome, saldo, senha = ""):
        print("Criando conta...")
        self._id = id
        self._nome = nome
        self.__saldo = saldo
        self.saldo = saldo

        if senha.strip() ==  "":
            self.__hash = self.pede_senha()

        else:
            self.__hash = ph.hash(senha)

        print(f"Conta criada com sucesso. Saldo atual de R$ {self.__saldo:.2f}")


    def pede_senha(self):
        from pwinput import pwinput
        senha = input(pwinput("escolha uma  senha: "))

        senha = ph.hash(senha)

        return senha


    def validar_senha(self, valor):
        try:
            ph.verify(self.__hash, valor)

            return True
        
        except VerificationError:
            return False

    def depositar(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise ValueError("Valor inválido para depósito.")

        if valor <= 0:
            raise ValueError("Valor inválido para depósito.")

        self.__saldo += valor

    def sacar(self, valor, chave):
        sucesso = self.validar_senha(chave)

        if sucesso:
            if not isinstance(valor, (float, int)):
                raise ValueError("Valor inválido para saque.")

            if valor <= 0 or valor > self.__saldo:
                raise ValueError("Valor inválido para saque.")
            
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            
        else:
            print("Saque negado. senha incorreta.")

        


        