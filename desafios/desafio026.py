from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto,):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_minimo = 1612
        self.inss = 7.5

    def analisar_salario(self):
        return self.sal_bruto / self.sal_minimo

    @abstractmethod
    def calc_salario(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, sal_hora, qtd_hora):
        sal_bruto = sal_hora * qtd_hora
        super().__init__(nome, sal_bruto)

    def calc_salario(self):
        return self.sal_bruto - (self.inss / 100 * self.sal_bruto)

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_salario(self):
        return self.sal_bruto - (self.inss / 100 * self.sal_bruto)


f1 = FuncionarioHorista("Paulo", 12, 200)
print(f"O sálario de {f1.nome}({f1.__class__.__name__}) é de {f1.calc_salario():.2f} e corresponde a {f1.analisar_salario():.1f} sálarios mínimo.")

f2 = FuncionarioMensalista("Amanda", 9500)
print(f"O sálario de {f2.nome}({f2.__class__.__name__}) é de {f2.calc_salario():.2f} e corresponde a {f2.analisar_salario():.1f} sálarios mínimo.")
