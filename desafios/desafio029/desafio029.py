from rich import print
class Diario:
    def __init__(self, senha = "12345"):
        self.__senha = senha
        self.__segredos = []

    def escrever(self, mensagem):
        self.__segredos.append(mensagem)

    def ler(self, senha = None):
        if senha == self.__senha:
            print(f"[green]Diário Liberado![/]")
            for mensagem in self.__segredos:
                print(f"- {mensagem}")
        else:
            raise PermissionError("Você não pode ler meu diário.")

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha.")

    @senha.setter
    def senha(self, dados):
        senha_antiga, senha_nova = dados

        if senha_antiga == self.__senha:
            self.__senha = senha_nova
            print("A senha foi trocada com sucesso.")

        else:
            print(f"Senha antiga errada, a troca de senha foi recusada")