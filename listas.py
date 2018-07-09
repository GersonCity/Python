# Listas

courses = ['Historia', 'Mate', 'Fisica', 'Biologia']
courses_2 = ['Arte', 'Educacion']
Nums = [1, 5, 2, 4, 3]

# Trae el ultimo valor de la lista
#   print(courses[-1])

# Trae lo que esta entre el primero de la lista y 2, pero no trae Fisica
#   print(courses[0:2])

# Agrega un valor a la ista
#   courses.append('Arte')
#   courses.append(courses_2)

# Agrega un valor a la lista al princio si se define como 0
#   courses.insert(0,'Arte')

# Agrega multiples valores a la lista como una lista dentro de otra lista
#   courses.insert(0, courses_2)

# Agrega una lista a otra como variables al final
#   courses.extend(courses_2)

# Remueve un valor de la lista
#   courses.remove('Mate')

# pop por defecto remueve el ultimo valor de la lista
#   courses.pop()

# Toma el ultimo valor de la lista y lo almacena en la variable y lo remueve de la lista
#   popped = courses.pop()
#   print(popped)

# Imprime lista al revez
#   courses.reverse()

# Imprime lista alfabeticamente o en orden asc
#   courses.sort()
#   Nums.sort()
#   sorted_courses = sorted(courses)
#   print(sorted_courses)

# Imprime lista desc orden
#   courses.sort(reverse=True)
#   Nums.sort(reverse=True)

# print(Nums)

# Simple For
# for item in courses:
#    print(item)

# FOR con index, enumera la lista ; start=1 indica que el index empieza en 1
# for index, course in enumerate(courses, start=1):
#    print(index, course)

# Imprime la lista como string separado por coma
#   course_str = ', '.join(courses)

# Deja la lista original
#   new_list = course_str.split(' - ')
#   print(course_str)
#   print(new_list)

######## TUPLES ###########

# Mutable
# list_1 = ['Historia', 'Mate', 'Fisica', 'Biologia']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Arte'

# print(list_1)
# print(list_2)

# Immutable

# Tuple no se puede mutar lista
# tuple_1 = ('Historia', 'Mate', 'Fisica', 'Biologia')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Arte'

# print(tuple_1)
# print(tuple_2)


########### SET ############
# Despliega lista pero  lo hace de manera desordenada pero no muestra duplicados

cs_courses = {'Historia', 'Mate', 'Fisica', 'Biologia', 'Mate'}
art_courses = {'Historia', 'Mate', 'Arte', 'Diseño'}

# Compara ambos sets y muestra los relacionados
print(cs_courses.intersection(art_courses))

# Muestra los valores que no estan en art_courses
print(cs_courses.difference(art_courses))

# Une ambos sets
print(cs_courses.union(art_courses))

# empty list
empty_list = []
empty_list = list()

# empty TUPLES
empty_tuples = ()
empty_tuples = tuple()

# Empty SETS
empty_set = {} # esto no esta bien, actualmente creara un diccionario vacio
empty_set = set()
