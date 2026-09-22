from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()

class Senha:
    def __init__(self):
        self.__hash = None
    
    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash =  ph.hash(chave)
        else:
            raise ValueError("Senha inválida")


    def validar(self, chave):
        try:
            ph.verify(self.__hash, chave)
            print("Senha correta, acesso liberado.")

        except VerifyMismatchError:
            print("Senha incorreta, acesso negado.")



        
