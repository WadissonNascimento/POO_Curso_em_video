from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET

class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Arquivo(ABC):
    @abstractmethod
    def exportar(self, lista: list) -> list|dict:
        pass


class JSON(Arquivo):
    def exportar(self, lista):
        dados = []
        if all(isinstance(item, Aluno) for item in lista):
            for aluno in lista:
                dados.append({
                    "aluno":aluno.nome,
                    "curso":aluno.curso,
                    "serie":aluno.serie
                })
            print(json.dumps(dados, ensure_ascii=False, indent=4))

        if all(isinstance(item, Usuario) for item in lista):
            for aluno in lista:
                dados.append({
                    "nome":aluno.nome,
                    "email":aluno.email
                })
            print(json.dumps(dados, ensure_ascii=False, indent=4))


class XML(Arquivo):
    def exportar(self, lista):
        raiz = ET.Element("dados")

        if all(isinstance (item, Aluno) for item in lista):
            for objeto in lista:
                item = ET.SubElement(raiz, "Aluno")

                for atributo, valor in objeto.__dict__.items():
                    campo = ET.SubElement(item, atributo)
                    campo.text = str(valor)

            ET.indent(raiz, space="    ")
            print(ET.tostring(raiz, encoding="unicode"))

        if all(isinstance (item, Usuario) for item in lista):
            for objeto in lista:
                item = ET.SubElement(raiz, "Usuario")

                for atributo, valor in objeto.__dict__.items():
                    campo = ET.SubElement(item, atributo)
                    campo.text = str(valor)
                    
            ET.indent(raiz, space="     ")
            print(ET.tostring(raiz, encoding="unicode"))


def exportar_dados(objeto, lista):
    objeto.exportar(lista)

