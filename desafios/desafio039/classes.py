from abc import ABC, abstractmethod
import re

class Validar(ABC):
    @abstractmethod
    def validar(self, valor):
        pass


class Usuario(Validar):
    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, valor):
            return True

        else:
            return False

class Email(Validar):
    def validar(self, valor: str) -> bool:
        regex = r"^[a-z0-9_%=-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
        if re.fullmatch(regex, valor):
            return True

        else:
            return False

class Senha(Validar):
    def validar(self, valor):
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%$?]).{8,}"
        if re.fullmatch(regex, valor):
            return True

        else:
            return False

def validar_dados(objeto, valor):
    if objeto.validar(valor):
        print(f"O valor {valor} é valido: SIM")
    else:
        print(f"O valor {valor} é valido: NÃO")