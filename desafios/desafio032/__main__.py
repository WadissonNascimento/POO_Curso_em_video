from desafio032 import ContaBancaria
from rich import inspect

def main():
    cc = ContaBancaria(123, "Wadisson", 454, "gafanhoto")

    cc.sacar(500, "cu")

    inspect(cc, private=True, methods=True)
if __name__ == "__main__":
    main()