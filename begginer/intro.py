# import my_module as mm  # Le podemos poner alias a los modulos para llamarlos mas facil
from my_module import find_index, test  # otra manera de llamar al modulo, pero especificando que se necesita llamar.
import random
import datetime
import calendar
import os  # acceso a rutas, escanea filesystem, delete, create files, etc.
import sys


cursos = ['Historia', 'Arte', 'Fisica', 'Computacion']

# index = mm.find_index(cursos, 'Arte') # con alias
index = find_index(cursos, 'Arte')  # sin alias
print(index)
print(test)  # imprime la variable test que esta en el modulo my_module.py

# print(sys.path)
'''con eso vemos la ruta donde esta trayendo los modulos '''

random_cursos = random.choice(cursos)

print(random_cursos)

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))  # Trae año bisiesto

print(os.getcwd())  # imprime el diectorio actual en cual estamos trabajando
print(os.__file__)  # imprime las librerias de python
