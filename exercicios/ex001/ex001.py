#declaração de classes
class Gafanhoto:
    def __init__(self): #método construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0
        self.sexo = None

    #métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} e é do sexo {"Indefinido" if self.sexo == None else self.sexo}."


#declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.sexo = "Feminino"
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.sexo = "Masculino"
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())