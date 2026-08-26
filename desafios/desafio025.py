from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0 

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        fator = 0.50

        return f"O valor do frete da entrega de moto fica R${fator * self.distancia} para a distancia de {self.distancia}KM."


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            return "Mínimo de 50km para entrega de caminhão."

        fator = 1.20
        return f"O valor do frete da entrega de caminhão fica R${fator * self.distancia} para a distancia de {self.distancia}KM."


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return "Máximo de 10km para entrega de drone."

        fator = 9.50

        return f"O valor do frete da entrega de drone fica R${fator * self.distancia} para a distancia de {self.distancia}KM."


t1 = Moto(10)
t2 = Caminhao(50)
t3 = Drone(10)

print(t1.calc_frete())
print(t2.calc_frete())
print(t3.calc_frete())
    
