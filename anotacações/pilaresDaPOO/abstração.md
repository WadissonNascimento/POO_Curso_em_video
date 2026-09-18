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