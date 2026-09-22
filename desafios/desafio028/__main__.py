from desafio028 import Termostato
from rich import print, inspect

def main():
    t1 = Termostato()
    t1.temperatura = 29
    inspect(t1, methods=True, private=True)

if __name__ == "__main__":
    main()