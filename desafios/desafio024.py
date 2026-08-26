from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("---iniciando prepararo---")
        print(f"1. {self.ferver_agua()} ")
        print(f"2. {self.misturar()} ")
        print(f"3. {self.servir()} ")
        print("---bebida pronta---")

    def ferver_agua(self):
        return "Fervendo água a 100 graus Celsius."


    @abstractmethod
    def misturar():
        pass

    @abstractmethod
    def servir():
        pass


class Cafe(BebidaQuente):
    def misturar(self):
         return "passando água pressurizada pelo pó de cafe moido."

    def servir(self):
        return "Servindo em xícara pequena."
class Cha(BebidaQuente):
    def misturar(self):
        return "Mergulhar sache de ervas na água."

    def servir(self):
        return "Servindo  na caneca  de porcelana com limão."


class Leite(BebidaQuente):
    def misturar(self):
        return "Passando água pressurizada pelo bico do leite."

    def servir(self):
        return "Servindo na caneca grande já com café."

b1 = Cafe()
b2 = Cha()
b3 = Leite()
b1.preparar()
b2.preparar()
b3.preparar()

    
        


        