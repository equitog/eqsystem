import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
""" Parametros de acceso a origenes de datos. Archivos Planos """

PLAIN = {
    "CSV": {
        "ROOT": ROOT_DIR,
        "NAME": "Key_access",
        "SEP": ";"
    }
}

""" Parametros de acceso a origenes de datos. Tablas """
DATABASES = {
    "default": {
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "SCHEMA": ""
    }
}
