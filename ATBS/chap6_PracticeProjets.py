# Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(Tabla):
    colWidths = [0] * len(Tabla)  # Con esto identificamos el total de listas internas y se lo asignamos como el total de columnas, eje: tableData tiene 3 listas = 3 columnas
    # print(str(colWidths))
    # for v in Tabla:
    #     print(v)
    # print(k[1].center(5), end='')
    for j in range(len(Tabla[0])):  # Recorre el largo de la primera lista
        # print(j) # imprime el numero de listas
        for i in range(len(Tabla)):  # Recorre el total de listas
            # print(i) # Imprime el numero de items en la lista
            print(Tabla[i][j].center(7), end='')  # Imprime
        print()


printTable(tableData)
