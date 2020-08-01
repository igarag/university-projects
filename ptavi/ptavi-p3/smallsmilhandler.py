#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#Ignacio Arranz Agueda - ISAM - PTAVI - Practica 3 (3)

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        # Declaramos la lista
        self.elementos = []
        self.tags = ["root-layout", "region", "img", "audio", "textstream"]
        self.atributos = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "bottom", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
        }

    def get_tags(self):
    # Devuelve una lista con etiquetas, atributos y contenidos encontrados
        return self.elementos

    def startElement(self, name, attrs):
        self.diccionario = {}
        if name in self.tags:
            self.diccionario['etiqueta'] = name
            for atributo in self.atributos[name]:
                self.diccionario[atributo] = attrs.get(atributo, "")
            self.elementos.append(self.diccionario)
#============PROGRAMA PRINCIPAL=====================
if __name__ == "__main__":
    parser = make_parser()
    myHandler = SmallSMILHandler()
    parser.setContentHandler(myHandler)
    parser.parse(open('karaoke.smil'))
    print myHandler.get_tags()
