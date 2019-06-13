import pandas as pd
from setting import PLAIN
import json as js


class UseSetting:
    path = ''
    file_name = ''


    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        print("""RUTA DE ACCESO:\t\t{ruta}
NOMBRE ARCHIVO:\t\t{nombre}""".format(ruta=self.path, nombre=self.file_name))

    def __del__(self):
        print("Espacio libre: UseSetting")

class Source(UseSetting):
    def __del__(self):
        print("Espacio libre: Source")

a = UseSetting(PLAIN['CSV']['ROOT'], PLAIN['CSV']['NAME'])