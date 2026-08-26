from abc import ABC, abstractmethod
from random import randint

class Personagem(ABC):
    def __init__(self, nome, vida, armadura, dano):
        self.nome = nome
        self.vida = vida
        self.armadura = armadura
        self.dano = dano


    def rolar_dados(self):
        return randint(1, 20)

    def atacar(self, alvo):
        dado = self.rolar_dados()
        print(f"dado: {dado} ")

        if dado < 10:
            return "Você errou o ataque."

        
        dano = dado + self.dano

        if dado > 18:
                    dano += 10

        alvo.receber_dano(dano)

        return f"{self.nome} deu {dano} de dano em {alvo.nome}, agora ele esta com {alvo.vida}."

    def receber_dano(self, dano):
        dano = dano / self.armadura
        self.vida -= dano
        return f"{self.nome} acaba de receber {dano} de dano e agora esta com {self.vida}."

    @abstractmethod
    def curar(self):
         pass

    
class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        armadura = 15
        dano = 20
        super().__init__(nome, vida, armadura, dano)
        

    def curar(self):
        self.vida = self.vida + self.vida / 2 
        return f"{self.nome} acabou de se curar com esparadrapos, agora esta com {self.vida} pontos de vida."

class Mago(Personagem):
    def __init__(self, nome, vida):
        armadura = 5
        dano = 35
        super().__init__(nome, vida, armadura, dano)

    def curar(self):
        self.vida = self.vida + self.vida / 2 
        return f"{self.nome} acabou de ser curar com uma poção de cura, agora esta com {self.vida} pontos de vida."



p1 = Guerreiro("Kratos", 2000)
p2 = Mago("Merlin", 1000)

print(p1.atacar(p2))
print(p2.curar())
print(p2.atacar(p1))