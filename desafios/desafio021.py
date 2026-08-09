from rich import print

class Caneta:
    def __init__(self, cor_caneta):
        self.cor = cor_caneta
        self.tampada = True


    def escrever(self, frase):
        if self.tampada:
            return f"A caneta esta tampada, destampe antes de escrever"
        
        return f"[{self.cor.strip()}]{frase}[/]"


    def destampar(self):
        self.tampada = False
        print("Você acaba de destampar a caneta!")

    def tampar(self):
        self.tampada = True
        print("Você acaba de tampar a caneta!")




c1 = Caneta("blue")
c1.destampar()
print(c1.escrever("Olá, Mundo!"))
c1.tampar()
print(c1.escrever("Guanabara"))
