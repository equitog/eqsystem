import pandas as pd
import os
from setting import PLAIN


class UseSetting:
    path = PLAIN['CSV']['ROOT']
    file_name = PLAIN['CSV']['NAME']
    file_sep = PLAIN['CSV']['SEP']


#     def __init__(self, path, file_name, sep):
#         self.path = path
#         self.file_name = file_name
#         self.file_sep = sep
#         print("""RUTA DE ACCESO:\t\t{ruta}
# NOMBRE ARCHIVO:\t\t{nombre}""".format(ruta=self.path, nombre=self.file_name))

    def getcolumn(self):

        f = pd.read_csv(os.path.join(self.path, self.file_name + '.csv'), sep=self.file_sep)

        return f


class Source(UseSetting):
    pass

