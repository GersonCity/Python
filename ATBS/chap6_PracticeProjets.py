# Table Printer


def printTable(Tabla):
    colWidths = [0] * len(Tabla)  # COn esto identificamos el total de listas internas y se lo asignamos como el total de columnas, eje: tableData tiene 3 listas = 3 columnas
    print(colWidths)
    for k in Tabla:
        # print(k.ljust(colWidths, ' '))
        # print(k[0].rjust(colWidths, ' '), end=' ')
    # print(Tabla)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)


# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)
