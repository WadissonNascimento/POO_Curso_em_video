from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario: int|float):
        self.nome = nome
        self._salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario: float|int):
        if novo_salario is None:
            raise ValueError("Impossivel reajustar o salario desse jeito.")
    
        else:
            if novo_salario < self._salario:
                raise PermissionError("Você não pode abaixar o salário do funcionario.")

            else:
                self._salario = novo_salario

    def __str__(self):
        return f"O funcionario {self.nome} tem o sálario de R${self._salario} e receberá um bonus de {self.calcular_bonus}"

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.15

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
       return self._salario * 0.10

class Designer(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.08
