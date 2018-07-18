# LISTAS

catNames = []

while True:
    print('Ingrese el nombre del gato ' + str(len(catNames) + 1) + '(o no ingrese nada para salir.):')
    name = input()  # Parametro de entrada y donde almacenamos nuestro valor que escribimos
    if name == '':  # validamos si lo que escribimos esta vacio y se sale del cliclo
        break
    catNames = catNames + [name]  # Concatenacion de lista

print('Los nombres de los gatos son: ')

for name in catNames:  # imprimimos todos los valores que se encuentran en la lista catNames
    print('  ' + name)

# For loop con listas
    # range(len(someList)) with a for loop to iterate over the indexes of a list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# Validamos que un valor este en la lista al escribir.
myPets = ['Zophie', 'Pooka', 'Fat-Tail']
print('Ingrese nombre de mascota')
name = input()

if name not in myPets:
    print('No tengo una mascota con ese nombre')
else:
    print(name + ' es mi mascota.')

# Multiple Assignment Trick
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

# METODOS

# encontrando un valor en una lista con el metodo index()
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')

# agregado valores a una lista usando los metodos append() y insert() --> estos metodos solo se ocupan en listas
spam = ['cat', 'dog', 'bat']
spam.append('moose')  # Agrega el valor al final de la lista
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')  # Inserta el valor en el index seleccionado(1) desopues de "cat"
print(spam)

# Eliminando valores en una lista con el metodo remove()
# metodo del() es bueno usar cuando se sabe el index en la lista y remove() cuando se sabe el valor en la lista

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('cat')
print(spam)

# ordenando valores con el metodo sort()
spam = [2, 5, 3.14, 1, -7]
spam.sort()  # ascendente
# spam.sort(reverse=True)  # desc
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# orden alfabetico
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)

# Example Program: Magic 8 Ball with a List
import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])


# Mutable y no mutable data type

# No mutable
name = 'Zophie a cat'
name[7] = 'the'

# Mutable
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)


# TUPLES son listas que no se pueden modificar
newTuple = ('hola', 40, 0.5)


type(('hola',))  # con esto mostramos que el valor es un tuple, al poner una coma(,) al final del string
type(('hola'))  # indica el valor del string en este caso -> str

# Converting Types with the list() and tuple() Functions
tuple(['cat', 'dog', 5])  # ('cat', 'dog', 5)
list(('cat', 'dog', 5))  # ['cat', 'dog', 5]
list('hello')            # ['h', 'e', 'l', 'l', 'o']
# Converting a tuple to a list is handy if you need a mutable version of a tuple value.

# References

# Pasamos la lista spam a cheese, pero ambas quedan con el mismo ID, son la misma lista, al modificar una, se modifican ambas
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hola!'
print(spam)
print(cheese)

# Passing References

deff eggs(someParameter):
    someParameter.append('Hola!')

spam = [1, 2, 3]
eggs(spam)
print(spam)


# The copy Module’s copy() and deepcopy() Functions
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy(). The deepcopy() function will copy these inner lists as well.


Practice Questions

Q: 1. What is []?
R: Esto es un lista

Q: 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains[2, 4, 6, 8, 10].)
R:
spam = [2, 4, 6, 8, 10]
spam[2] = 'hello'
print(spam)


For the following three questions, let’s say spam contains the list['a', 'b', 'c', 'd'].

Q: 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
R:

Q: 4. What does spam[-1] evaluate to?
R: 'd'

Q: 5. What does spam[:2] evaluate to?
R: muestra desde el valor 0 hasta el 1 = a, b


For the following three questions, let’s say bacon contains the list[3.14, 'cat', 11, 'cat', True].

Q: 6. What does bacon.index('cat') evaluate to?
R: 1

Q: 7. What does bacon.append(99) make the list value in bacon look like?
R: [3.14, 'cat', 11, 'cat', True, 99]

Q: 8. What does bacon.remove('cat') make the list value in bacon look like?
R: [3.14, 11, 'cat', True]

Q: 9. What are the operators for list concatenation and list replication?
R: el operador para concatenar listas es + y para replicar *

Q: 10. What is the difference between the append() and insert() list methods?
R: que apped() agrega un valor al final de la lista e insert() lo agrega dependiendo el index que se le asigne

Q: 11. What are two ways to remove values from a list?
R: remove() y del statement

Q: 12. Name a few ways that list values are similar to string values.
R: Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

Q: 13. What is the difference between lists and tuples?
R: que las litas se pueden modificar sus valores y los tuples no.

Q: 14. How do you type the tuple value that has just the integer value 42 in it?
R: (42,)

Q: 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
R: tuple() y list()

Q: 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
R: Contienen References hacia los valores de una lista

Q: 17. What is the difference between copy.copy() and copy.deepcopy()?
R: que copy() copia la lista en una nueva lista y deepcopy() copia la lista si es que una lista tiene mas listas adentro
