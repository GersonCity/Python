# Comma Code

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']


def commaCode(formatLista):

    popped = formatLista.pop()  # toma el ultimo valor de la lista y lo guarda en una variable
    # ultimoValor = 'and' + r.rsplit(',', 1)[1]  # obtengo el ultimo valor y le agrego un "and" antes.
    ultimoValor = 'and ' + popped
    formatLista.append(ultimoValor)
    result = ', '.join(formatLista)  # Dejo la lista como un string y le agrego comas
    print(result)


# commaCode(spam)


# Character Picture Grid
    #
    #
    #
    #
    # Y
grid = [['.', '.', '.', '.', '.', '.'],  # <------- X
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

corazon = []
n = len(grid)
print(n)

for a in grid[x][y]:
    print(a)
    for b in grid[x][y]:
        print(a, b)
