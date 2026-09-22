from desafio029 import Diario
from rich import print, inspect

def main():
    d1 = Diario("Gafanhoto")

    d1.escrever("Olá, Mundo!")
    try:
        d1.ler("Gafanhoto")

    except Exception as e:
        print(f"[red]ERRO: {e}[/]")

    d1.senha = "Gafanhoto",  "alibaba"

    try:
        d1.ler("Gafanhoto")

    except Exception as e:
        print(f"[red]ERRO: {e}[/]")

    inspect(d1, private=True, methods=True)

if __name__ == "__main__":
    main()