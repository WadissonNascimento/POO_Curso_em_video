from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados


    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def calcular_perimetro(self):
        perimetro = 2 * 3.14 * self.raio

        return perimetro
   
    def calcular_area(self):
        area =  3.14 * self.raio * self.raio

        return area

class Quadrado(Poligono):
    def __init__(self, qtd_lados = 1):
        super().__init__(4)
        self.qtd_lados = qtd_lados

    def calcular_area(self):
        area = self.qtd_lados * self.qtd_lados

        return area

    def calcular_perimetro(self):
        perimetro = self.qtd_lados * 4

        return perimetro


p1 = Quadrado(12)
print(f"perimetro = {p1.calcular_perimetro():.2f}mm")
print(f"area = {p1.calcular_area():.2f}mm")