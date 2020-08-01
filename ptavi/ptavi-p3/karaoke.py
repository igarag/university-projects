#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Ignacio Arranz Agueda - ISAM - PTAVI - Practica 3 (5)

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import os


class KaraokeLocal():
    def __init__(self, fich):
        smallsmilhandler = SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(smallsmilhandler)
        parser.parse(open(fich))
        self.lista = smallsmilhandler.get_tags()

    def __str__(self):
        out = ""
        for elemento in self.lista:
            name = elemento['etiqueta']
            out += name
            for atributo in elemento:
                if atributo != "etiqueta" and elemento[atributo] != "":
                    out += "\t" + atributo + ":" + elemento[atributo]
            out += "\n"
        return out

    def do_local(self):
        for elem_diccionario in self.lista:
            name = elem_diccionario['etiqueta']
            for atributo in elem_diccionario:
                if atributo == "src":
                    resource = elem_diccionario['src']

                    os.system("wget -q " + resource)
                    resource = resource.split("/")[-1]

                    elem_diccionario["src"] = resource
        return self.lista
#=========================PROGRAMA PRINCIPAL============================
if __name__ == "__main__":
    try:
        fich = sys.argv[1]
    except IndexError:
        print "Usage: python karaoke.py file.smil"
    karaokelocal = KaraokeLocal(fich)
    print karaokelocal
    karaokelocal.do_local()
    print karaokelocal
