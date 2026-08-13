# Os 4 pilares da programação orientada a objetos

## Abstração
É a pratica de ignorar o irrelevante e se focar estritamente no essencial.

### Principais vantagens
- Maior legibilidade;
- Padronização;
- Simplificação;
- Segurança.

Existe abstração de dados, que acontece quando ignoramos informações desnecessárias para o escopo do projeto.

Existe a abstração de processos, quando não precisamos saber como um método faz seu trabalho, apenas sabe que ele existe pela interface.

Classe abstrata = classe que serve de base para as classes filhas, ela não vai virar um objeto mas serve de base para as subclasses que vão.

Método concreto = fazer_aniversario()

Método abstrato = estudar() {abstract}

Ao Definir um conjunto de métodos abstratos, dizemos que estamos criando a interface pública da classe.

Uma classe abstrata pode ter métodos abstratos que deverão ser obrigatoriamente implementados nas subclasses.

Mas uma classe abstrata pode ter métodos concretos se eles funcionarem da mesma maneira para todas as subclasses(DRY).

ABC = Abstract Base Classes.

## Encapsulamento

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

##Polimorfismo 