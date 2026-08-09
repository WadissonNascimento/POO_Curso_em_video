class Funcionario:
    from rich import print
    def __init__(self, nome, cargo, setor, empresa="Curso em Video"):
        self.nome =  nome
        self.cargo = cargo
        self.setor = setor
        self.empresa = empresa

    def apresentar(self):
        return f"Olá me chamo {self.nome} sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}"


f1 = Funcionario("Pedro", "Programador", "TI")
print(f1.apresentar())