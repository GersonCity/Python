
import os  # acceso a rutas, escanea filesystem, delete, create files, mover archivos, cambiar ambientes, etc
from datetime import datetime
# print(dir(os)) # leemos el modulo

# print(os.getcwd())  # imprime el directorio actual del proyecto

os.chdir('/Users/exgciud/Desktop/')  # chdir = change directory

# Para crear un directorio, existen 2 formas
# os.mkdir('Python_2') # Solo crea el directorio especificado
# os.makedirs('Python_2/sub_directorio') # crea direcorio y sub directorios si se especifica

# Borrar directorios
# os.rmdir('Python_2')
# os.removedirs('Python_2/sub_directorio') # No borra los subdirectorios, solo borra el principal.

# Renombrar# os.makedirs('Python_2/sub_directorio')
# os.rename('test.py', 'test_2.py')

# print(os.stat('test_2.py'))  # imprimimos los stats del archivo.

# mod_time = os.stat('test_2.py').st_mtime
# print(datetime.fromtimestamp(mod_time))  # imprime la fecha formateada

# print(os.getcwd())
# print(os.listdir()) # Listamos todos los archivos, por defecto lista todo lo de os

# imprime todo lo que hay en la direccion, Ruta -> directorios -> archivos
# for dirpath, dirname, filenames in os.walk('/Users/exgciud/Desktop/'):
#     print('Current Path', dirpath)
#     print('Directories', dirname)
#     print('Files', filenames)
#     print()

# variables de ambientes
print(os.environ.get('USERPROFILE'))

file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))  # si existe la ruta
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))  # se usa para dividir la extension de un archivo
print(dir(os.path))
