# Comma Code

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']

# Solucion mia
def commaCode(formatLista):

    popped = formatLista.pop()  # toma el ultimo valor de la lista y lo guarda en una variable
    # ultimoValor = 'and' + r.rsplit(',', 1)[1]  # obtengo el ultimo valor y le agrego un "and" antes.
    ultimoValor = 'and ' + popped
    formatLista.append(ultimoValor)
    result = ', '.join(formatLista)  # Dejo la lista como un string y le agrego comas
    print(result)

commaCode(spam)

# Solucion stackoverflow https://stackoverflow.com/questions/38824634/automate-the-boring-stuff-with-python-comma-code)

def comma(items):
    for i in range(len(items) -2):
        print(items[i], end=", ")# minor adjustment from one beginner to another: to make it cleaner, simply move the ', ' to equal 'end'. the print statement should finish like this --> end=', '
    print(items[-2] + ' and ' + items[-1])

comma(spam)




# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],  # <------- X
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# Solucion 1 ( mi forma algo ajustada de stackoverflow)
rows = len(grid)
columns = len(grid[0])
# print(rows, columns)
for x in range(columns):
    for y in range(rows):
            print(grid[y][x], end='') # comando end es para que en el print no agrege una nueva linea, si no que la haga al lado
    print() # print blank line

# Solucion 2 ( https://stackoverflow.com/questions/30424355/automate-the-boring-stuff-with-python-chapter-4-exercise)
for j in range(len(grid[0])):  # Recorre el largo de la primera lista
    for i in range(len(grid)): # Recorre el total de listas
        print(grid[i][j],end='')
    print('')
