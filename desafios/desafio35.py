from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome, ext:str, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.extensao = ext
        
    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext):
        formatos = [".doc", ".pdf"]
        ext = ext.lower().strip()

        if ext in formatos:
            self._extensao = ext

        else:
            raise AttributeError("O arquivo está em um formato não suportado.")

    @property
    def nome_completo(self):
        return f"{self.nome + self.extensao} ({self.tamanho/1_000_000}MB)"
        

class Doc(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, ".doc",  tamanho)

    def abrir(self):
        print(f"Abrindo  o arquivo '{self.nome_completo}'no Microsoft Word")


class Pdf(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, ".doc", tamanho)

    def abrir(self):
        print(f"Abrindo  o arquivo '{self.nome_completo}' no Adobe Reader")


def abrir(objeto):
    objeto.abrir()


a = Doc("prova", 200_000)
a2 = Pdf("Gabarito", 1_000_000)

abrir(a)
abrir(a2)