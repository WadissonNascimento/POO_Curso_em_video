from desafio031 import Retangulo
from rich import print, inspect

def main():
    r = Retangulo(8, 4)

    r.altura = 15
    r._base = 15


    inspect(r, private=True, methods=True)

if __name__ == "__main__":
    main()