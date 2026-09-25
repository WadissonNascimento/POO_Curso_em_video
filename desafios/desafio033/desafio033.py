from abc import ABC 
from datetime import datetime


data_atual = datetime.today()
ano_atual = data_atual.year

class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self.nascimento = nascimento
        self._nome = nome

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano_nascimento: int):
        if not isinstance(ano_nascimento, int):
            raise ValueError("Digite um número inteiro!")

        if ano_nascimento > ano_atual:
            raise ValueError(f"O ano {ano_nascimento} é inválido!")

        if ano_atual - ano_nascimento > 110:
            raise ValueError(f"O ano {ano_nascimento} é inválido!")

        self._nascimento = ano_nascimento

    @property
    def idade(self):
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self):
        raise PermissionError("Você não tem permissão para mexer na idade, altere a data de nascimento.")


class Aluno(Pessoa):
    def __init__(self, nome: str, nascimento: int, curso: str):
        self.cursos_oficiais = ["ADS", "ADM", "ENG", "CONT"]
        self.curso = curso
        super().__init__(nome, nascimento)


    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso: str):
        for curso_oficial in self.cursos_oficiais:
            if curso_oficial == curso.strip().upper():
                self._curso = curso
                break
        else:
            raise ValueError(f"O curso {curso} não esta na lista.")


    def add_curso(self, curso: str):
        self.cursos_oficiais.append(curso)