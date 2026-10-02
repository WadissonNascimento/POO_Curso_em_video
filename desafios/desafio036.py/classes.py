from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor

        else: 
            raise ValueError("O pagamento so pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        return f"R$ {self._valor:.2f}"

    @abstractmethod
    def pagar(self, valor):
        pass


class Pix(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.fvalor} via PIX")

class CartaoDeCredito(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.fvalor} via CARTÃO DE CRéDITO")

class Boleto(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.fvalor} via BOLETO")


#DUCK TYPING
def finalizar_compra(objeto, valor):
    try: 
        p1 = objeto
        p1.pagar(valor)

    except Exception as e:
        print(f"achei um erro ao tentar pagar com {objeto}: {str(e)}")