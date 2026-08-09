#declaração de classes
class Gafanhoto:
    """
        Essa classe cria um Gafanhoto, que é uma pessoa que tem nome, idade e sexo

        Para criar uma pessoa, use
        variavel = Gafanhoto(nome, idade, sexo)
    """
    def __init__(self, n = "", i = "0", s = None): #método construtor
        #Atributos de instância
        self.nome = n
        self.idade = i
        self.sexo = s

    #métodos de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):# Dunder method
        return f"{self.nome} é um Gafanhoto(a) e tem {self.idade} e é do sexo {"Indefinido" if self.sexo == None else self.sexo}."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade} ; sexo = {self.sexo}"

#declaração de objetos
g1 = Gafanhoto("Maria", 17, "Feminino")
g1.aniversario()

print(g1.__dict__)#Atribute
print(g1.__getstate__())#method
print(g1.__class__)
