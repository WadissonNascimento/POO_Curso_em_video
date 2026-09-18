from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, nome_jogo):
        for jogo in self.jogos:
            if jogo.strip().lower() == nome_jogo.strip().lower():
                return f"Jogo não adicionado. O jogo {nome_jogo} já esta na lista de jogos favoritos."

        self.jogos.append(nome_jogo)
        return f"Jogo {nome_jogo} adicionado a lista de favoritos."
        
    def exibir_ficha(self):
        self.jogos = sorted(self.jogos, key=str.lower)
        jogos = "\n".join(f"• {jogo}" for jogo in self.jogos)
        ficha =  Panel(f"Nick: {self.nick}\nJogos favoritos:\n{jogos}", title=self.nome, width=50)
        return ficha
        

p1 = Gamer("Wadisson", "King Of Zueira")
print(p1.add_favoritos("Zelda"))
print(p1.add_favoritos("Dark Souls 1 remasted"))
print(p1.add_favoritos("Dark Souls 1 remasted"))
print(p1.exibir_ficha())

            