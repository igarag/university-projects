#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de práctica

Para ejecutarlo, desde la shell: 
 $ python check-p5.py login_laboratorio

"""

import os
import random
import sys


# Diccionario con la relación de nombres de usuario
# en los laboratorios (clave) y nombres de usuario en GitHub (valor)
github_dict = {
    "iarranz": "igarag",
    "smarin": "silviamaa",
    "miriammz": "miriammz",
    "rgalan": "raquelgalan",
    "jmarugan": "jfernandezmaru",
    "jcdb": "jcdb",
    "jcdb": "jcdb",
    "maferna": "mghfdez",
    "mtejedor": "mtejedorg",
    "apavo": "apavo",
    "oterino": "aoterinoc",
    "ndiaz": "nathdiaza",
    "crodrigu": "crodriguezgarci",
    "ilope": "ilope236",
    "opedraza": "olallasanchez",
    "calvarez": "calvarezpe",
    "dpascual": "dpascualhe",
    "avera": "Abel-V",
    "amoles": "alvaromv83",
    "aramas": "aramas",
    "jbaos": "JaviBM11",
    "rsierra": "rsierrangulo",
    "imalo": "nmalo5",
    "mireya": "mireepink",
    "albagc": "albagcs",
    "rpablos": "raquelpt",
    "cgarcia": "celiagarcia",
    "lyanezgu": "lyanezgu",
    "omarled": "auronff10",
    "roger": "rogerurrutia",
    "lsoria": "lsoriai",
    "zhiyuan": "ziyua",
    "mcapitan": "mcapitan",
    "juanmis": "Jmita", 
    "molina": "jmartinezmolina",
    "afrutos": "alejandrodefrutos",
    "molina": "jmartinezmolina",
    "carlos": "CarlosJLoH",
    "sagun": "caarrieta"
}


files = ['README.md',
         'LICENSE',
         'p5.txt',
         'sip.libpcap.gz',
         'p5.libpcap',
	 'check-p5.py',
         '.git']

aleatorio = str(int(random.random() * 1000000))

error = 0

repo_git = "http://github.com/" + github_dict[sys.argv[1]] + "/ptavi-p5/"

print "Clonando el repositorio " + repo_git + "\n"
os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    student_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = 1
    print "Error: No se ha creado el repositorio git correctamente."
    print 
    sys.exit()

if len(student_file_list) != len(files):
    error = 1
    print "Error en el número de ficheros encontrados en el repositorio"

for filename in files:
    if filename not in student_file_list:
        error = 1
        print "Error: " + filename + " no encontrado. Tienes que subirlo al repositorio."

if not error:
    print "Parece que la entrega se ha realizado bien."
    print "Recuerda que también tienes que realizar un test en Moodle."
    print
