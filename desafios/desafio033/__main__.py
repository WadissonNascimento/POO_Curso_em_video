from desafio033 import Aluno
from rich import inspect

def main():
    p1 = Aluno("Wadisson", 2005, "ADS")
    p1.add_curso("MODA")
    p1.curso = "MODA"
    

    inspect(p1, private=True, methods=True)


if __name__  == "__main__":
    main()