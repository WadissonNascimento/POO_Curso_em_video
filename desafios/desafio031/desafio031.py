class  Retangulo:
    def  __init__(self, base = 1 , altura = 1):
        self._base = None
        self._altura = None

        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @area.setter
    def area(self, valor):
        raise PermissionError("Você não pode definir a área")

    @property
    def medidas(self):
        return {
            "base":self.base,
            "altura":self.altura,
            "area":self.area
        }

    @medidas.setter
    def medidas(self, medidas):
        if not isinstance(medidas, tuple):
            raise TypeError("As medidas devem ser informadas dentro de uma tupla.")
        
        if len(medidas) != 2:
            raise SyntaxError("Informe uma tupla com apenas dois valores númericos")

        if isinstance (medidas[0], float) or isinstance(medidas[0], int):
            self.base = medidas[0]

        else:
            raise ValueError("Você precisa informar um número valido para a base")

        if isinstance (medidas[1], float) or  isinstance(medidas[1], int):
            self.altura = medidas[1]

        else:
            raise ValueError("Você precisa informar um número valido para a base")


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor deve ser um número.")

        if valor < 0:
            raise ValueError("Valor inválido para a base.")
        
        else:
            self._base = valor


    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor deve ser um número.")

        if valor < 0:
            raise ValueError("Valor inválido para a base.")

        else:
            self._altura = valor
