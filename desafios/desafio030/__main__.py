from desafio030 import Senha
from rich import print, inspect

def main():
    s1 = Senha()
    s1.senha = "wadisson"
    inspect(s1, private=True, methods=True)
    s1.validar("wadisson")

if __name__ == "__main__":
    main()