from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome_evento, qtd_pessoas):
        self.nome_evento = nome_evento
        self.qtd_pessoas = qtd_pessoas

    def analisar(self):
        if self.qtd_pessoas <= 0:
            print(f"Impossivel realizar os calculos com {self.qtd_pessoas} ou menos pessoas.")
            return 
        
        valor_carne_kg = 82.40 
        carne_por_pessoa = 0.400 

        carne_total = self.qtd_pessoas * carne_por_pessoa

        valor_total_carne = carne_total * valor_carne_kg
        valor_por_pessoa =  valor_total_carne / self.qtd_pessoas

        caixa = Panel(f'''Quantidade de carne recomendada: {carne_total}KG
Valor total das carnes: R${valor_total_carne}
Valor que cada pessoa devera pagar: R${valor_por_pessoa}\n''', title=f"{self.nome_evento}", width=50)
        print(caixa)

c1 = Churrasco("Churrasco da rapaziada", 200000)
c1.analisar()