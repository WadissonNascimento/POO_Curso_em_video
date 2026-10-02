class Produto:
    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor =  valor

    def __str__(self):
        return f"{self.nome} ({self.valor})"


class Carrinho:
    def __init__(self, produtos: list = None):
        self.lista_produtos = produtos if produtos else []

    @property
    def total(self):
        total = 0

        for produto in self.lista_produtos:
            total += produto.valor

        return f"R$ {total:.2f}"

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = "\n".join(str(p) for p in self.lista_produtos)
        return f"{itens}{linha}\nTotal: {self.total}"

    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.lista_produtos + [other])

        elif isinstance(other, Carrinho):
            return Carrinho(self.lista_produtos + other.lista_produtos)

        else:
            raise TypeError("Você tentou adicionar algo inválido no carrinho.")
