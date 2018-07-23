# Diccionarios y estuctrura de data

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])

# Diccionario vs una lista no estan ordenados como una lista, no estanxiste un "primero" en un diccionario

# Lista
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

# Diccionario
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

print(eggs == ham)

# Error al tratar de acceder a un indice que no existe en el diccionario, arrojara error Keyerror: 'color'

# spam = {'name': 'Zophie', 'age': 7}
# print(spam['color'])

# Ejemplo : Cumpleaños
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}  # creamos diccionario y usamos la key como nombres

while True:
    print("Ingresa un Nombre: (En blanco para salir)")
    name = input()
    if name == '':
        break

    if name in birthdays:  # validamos si el nombre que ingresamos existe en el diccionario con la key usando IN en.
        print(birthdays[name] + 'es el Cumpleaños de ' + name)
    else:
        print('No tengo informacion de Cumpleaños para ' + name)
        print('Cual es su cumpleaños?')
        bday = input()
        birthdays[name] = bday  # si no existe el nombre lo agregamos al diccionario
        print('Cumpleaños data actualizado.')


# The keys(), values(), and items() Methods

spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)
# Result
# red
# 42

for k in spam.keys():
    print(k)
# Result
# color
# age

for i in spam.items():
    print(i)
# Result
# ('color', 'red')
# ('age', 42)

# Mostrando como una lista
spam = {'color': 'red', 'age': 42}
print(spam.keys())
# result: dict_keys(['color', 'age'])
print(list(spam.keys()))  # esto toma el dict_keys que retorno spam.keys() y se lo pasa a list() el cual retorna los valores de la lista
# result: ['color', 'age']


# Asignando key y valor a variables separadas

spam = {'color': 'red', 'age': 42}

for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))

# The get() Method

picnicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('cups', 0)) + 'cups.')
# result : I am bringing 2cups.
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# result : I am bringing 0 eggs.  # Como no hay una key llamada 'eggs' el diccionario returna un valor por defecto de 0 debido al metodo get(), si no usamos get() el codigo causaria un error


# The setdefault() Method

spam = {'name': 'Poola', 'age': 5}

if 'color' not in spam:
    spam['color'] = 'black'

# el medoto setdefault() ofrece otra manera de de hacer lo que esta arriba con una linea de codigo.
spam = {'name': 'Poola', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam)
print(spam.setdefault('color', 'white'))  # asignamos denuevo un valor por defecto, pero el resultado sera black, ya que se habia asignado anteriormente y su key ya es 'black'


# Ejemplo : cuenta el numero de ocurrencia de cada letra en un string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


# Pretty Printing
import pprint  # imprta modulo para que al imprimir por pantalla salga de mejor manera(formateado), este modulo es muy util cuando un diccionario contiene listas anidadas y es engorroso leer.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
pprint.pformat(message)
print(pprint.pformat(message))

# A Tic-Tac-Toe Board // GATO

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# Nested Dictionaries and Lists

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():  # guest name es asignado a variable k y v alos items.
        numBrought = numBrought + v.get(item, 0)  # si el parametro item existe coomo un key en el diccionario lo asigna a v.
    return numBrought


print('Number of things being brought:')-
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(al]lGuests, 'apple pies')))
