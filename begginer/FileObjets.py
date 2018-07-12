# File Objets

# with open('exporta.sql', 'r') as f:  # esto nos permite trabajar con archivos dentro del blocke with, y no nos traemos que preocupar de tener que cerrarlos
# f_contents = f.read()
    for line in f:
       # f_contents = f.readline()
        print(line, end='')

# f = open('exporta.sql', 'r')  # 'r'(reading) para leer archivo

# print(f_contents)

# with open('test2.txt', 'w') as f:  # Crea archivo test2 ; w = write
#     f.write('test')  # escribe la palabra test en archivo
#     f.seek(0)  # sobreescibe la palabra test , pero si en la siguiente linea pones otra palabra o letra, la sobreescribe
#     f.write('test')

# Crea una copia de una archivo y crea otro.
with open('exporta.sql', 'r') as rf: # read file
    with open('exporta_copy.sql', 'w') as wf: # write file
        for line in rf:     # por cada linea en nuestro archivo original
            wf.write(line)  # escibe una linea en wf(exporta_copy)

# copiamos una imagen
with open('portal.png', 'rb') as rf:  # Al poner rb, estamos indicando que lea (r) un byte(b)
    with open('portal_copy.png', 'wb') as wf:  # write file
        chunk_size = 4096   # chunk = pedazo, es decir estamos indicando el tamaño del pedazo(de dato) que vamos a copiar
        rf_chunk = rf.read(chunk_size)  # estamos leyendo el chunk de nuestra foto
        while len(rf_chunk) > 0:  # cuando el largo de nuestro chunk sea mayor a 0, sigue leyendo
            wf.write(rf_chunk)   # copia el pedazo de data que esta en rf_chunk y lo copia al nuevo archivo(wf)
            rf_chunk = rf.read(chunk_size)  # leemos nuevamente el chunk para evitar un loop infinito y leemos el siguiente chunk
