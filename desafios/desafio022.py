from rich import print

class ControleRemoto:
    def __init__(self):
        self.tv_ligada = False
        self.volume = 0
        self.canal_atual = 0
        self.canais_disponiveis = [4, 5, 7]


    def ligar(self):
        if not self.tv_ligada:
            self.tv_ligada = True
            print("Você ligou a TV!")
            print(f"Canal atual: {self.canais_disponiveis[self.canal_atual]}")
            print(f"Volume atual: {self.volume}")


    def desligar(self):
        if self.tv_ligada:
            self.tv_ligada = False
            print("Você desligou a TV!")
        
    def aumentar_volume(self):
        if not self.tv_ligada:
            print("A tv esta desligada!")
            return 
        
        if self.volume == 100:
            print("100")
            return

        self.volume += 5
        print(f"volume: {self.volume}")


    def abaixar_volume(self):
        if not self.tv_ligada:
            print("A tv esta desligada!")
            return 
        
        if self.volume == 0:
            print(":muted_speaker:")
            return

        self.volume -= 5
        print(f"volume: {self.volume}")


    def passar_canal(self):
        if not self.tv_ligada:
            print("A tv esta desligada!")
            return 
        
        self.canal_atual += 1

        if self.canal_atual > 2:
            self.canal_atual = 0

        print(f"canal: {self.canais_disponiveis[self.canal_atual]}")


    def voltar_canal(self):
        if not self.tv_ligada:
            print("A tv esta desligada!")
            return 
        
        self.canal_atual -= 1

        if self.canal_atual < 0:
            self.canal_atual = 2

        print(f"canal: {self.canais_disponiveis[self.canal_atual]}")

c1 = ControleRemoto()
c1.ligar()
c1.passar_canal()
c1.passar_canal()
c1.passar_canal()
c1.voltar_canal()

for _ in range(21):
    c1.aumentar_volume()

for _ in range(21):
    c1.abaixar_volume()

c1.desligar()
c1.passar_canal()
c1.passar_canal()
c1.passar_canal()
c1.voltar_canal()

for _ in range(21):
    c1.aumentar_volume()

for _ in range(21):
    c1.abaixar_volume()
