
# Working with Key-Value Pairs

student = {'name': 'John', 'age': 25, 'Courses': ['Matematica', 'Computacion']}

# print(student['name'])

# student['telefono'] = '555555555'

# Si lo que estamos trayendo del diccionario(key) no esta lo controlamos con un get
# print(student.get('telefono', 'No encontrado'))

# update valor
# student['name'] = 'Jane'

# update muchos valores
# student.update({'name': 'Jane', 'age': 26, 'telefono': '6666666'})

# Borramos un valor especifico usando el key
# del student['age']

# Borra Age del diccionario y lo guarda en variable age
# age = student.pop('age')

# print(student)
# print

# imprime los keys del diccionario
# print(student.keys())

# imprime los valores del diccionario
# print(student.values())

# imtrime key y valores del diccionario
# print(student.items())

# Muestra valores y key mediante FOR
for key, value in student.items():
    print(key + ':', value)
