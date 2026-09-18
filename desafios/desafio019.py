from rich import print
from time import sleep
from rich.traceback import install

install()

class Livro:
    def __init__(self, nome_livro, qtd_paginas):
        self.nome_livro = nome_livro
        self.qtd_paginas = qtd_paginas
        self.pagina_atual = 1
        print(f"Você acabou de abrir o livro {self.nome_livro} que tem {self.qtd_paginas} páginas \nVocê esta ná pagina {self.pagina_atual}")

    def passar_pagina(self, valor):
        if self.pagina_atual == self.qtd_paginas:
            sleep(0.5)
            print("[red]Você esta na ultima do livro não é possivel avançar mais.[/]")
            return 
        
        contador = 0

        if valor <= 0:
            print(f"Não é possivel passar {valor} páginas.")
            return

        for pagina in range(1, valor+1):
            if self.pagina_atual == self.qtd_paginas:
                print(f'Você pulou {contador} páginas e esta na página {self.pagina_atual}.')
                print("[red]Você esta na ultima pagina do livro não tem como avançar mais.[/]")
                return
            
            self.pagina_atual += 1
            sleep(0.5)
            print(f"pag {self.pagina_atual} :right_arrow:  ", end="")
            contador += 1

        sleep(0.5)
        print(f'Você pulou {contador} páginas e esta na página {self.pagina_atual}.')

        
            


l1 = Livro("10 coisas que aprendi.", 2000)
l1.passar_pagina(-5)
l1.passar_pagina(10)
l1.passar_pagina(100)
l1.passar_pagina(100)