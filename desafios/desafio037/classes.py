from rich import print
from rich.panel import Panel 


class Mensagem:
    def __init__(self, msg, tipo, icone = ":speech_balloon:"):
        self._tipo = tipo
        self._mensagem = msg
        self._icone = icone 

    def mostrar(self):
        msg = Panel(
                self._mensagem,
                title=f"{self._icone} {self._tipo} {self._icone}", style="white on black", width=50
            )
        print(msg)

class Erro(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "Alerta", ":prohibited:")

    def mostrar(self):
         msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo} {self._icone}", style="yellow on red", width=50)
         print(msg)

class Alerta(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "Erro", ":warning:")

    def mostrar(self):
         msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo} {self._icone}", style="red on yellow", width=50)
         print(msg)
         
