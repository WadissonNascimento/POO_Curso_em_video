class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a porta")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda documentação para abrir um cnpj")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separare as partes sobre  uma  frigideira.")

class Pedra:
    pass


#MÉTODO PYTHONICO POLIMORFO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()

    except:
        print(f"Encontrei problemas ao tentar abrir {objeto.__class__.__name__}")