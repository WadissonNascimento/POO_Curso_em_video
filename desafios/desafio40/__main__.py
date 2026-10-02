from classes import *

a = [
    Aluno("Lucas", "ADS", 2),
    Aluno("Mariana", "Engenharia de Software", 3),
    Aluno("Pedro", "Ciência da Computação", 1)
]

u = [
    Usuario("Ana", "ana@gmail.com"),
    Usuario("Bruno", "bruno@gmail.com"),
    Usuario("Carla", "carla@gmail.com")
]


exportar_dados(XML(), u)