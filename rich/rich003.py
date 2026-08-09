from rich import print, inspect
from rich.table import Table

tabela = Table()

tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("Preço", justify="center", style="blue")

tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "[green]R$5,00[/]")
