## Herança
É um relacionamento entre itens gerais(ancestrais) e tipos mais especificos(descendentes) desses itens que herdam  atributos e métodos dos niveis superiores.

### Principais vantagens:
- Reutilização de código;
- Organização hierárquica;
- Facilita manutenção;
- Extensibilidade;
- Suporte polimorfismo.

### Terminologia
- #### Passarinho Pai = Super classe
    - Classe Base 
    - Classe Ancestral
    - Classe mãe
#####   ^
#####   |
- #### herança
    - Generalização
    - Relação tipo "é um"
#####    |
#####    v
- #### Passarinho Fiho = Subclasse
    - Classe derivada
    - Descendente 
    - Classe filha

### Código
```python
from rich import print, inspect
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
      self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de se matricular.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Professor {self.nome} começou a dar aula.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater o ponto.")

a1 = Aluno("José", 21, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Samuel", 22, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Emilly", 20, "Diretora", "Diretoria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1)
```