"""
def funcion_1():  # Definiendo una funcion
    # pass  # Esto significa que por el momento no haremos nada con esta funcion, pero mas adelant agregaremos cosas
    print('Hola Funcion!')


funcion_1()  # Llamada a funcion


def funcion_2():
    return 'Hola Funcion 2!'


print(funcion_2())
print(funcion_2().upper())  # Trae todo en mayyusculas


def funcion_3(saludos, nombre='Tu'):  # Le pasamos parametro a la funcion
    # return '{} Funcion 3!.'.format(saludos)
    return '{}, {}'.format(saludos, nombre)


print(funcion_3('Hola', nombre='Gerson'))


def studen_info(*args, **kwargs):  # args muestra como lista y kwargs como diccionrio
    print(args)
    print(kwargs)


studen_info('Mate', 'Arte', name='John', age=22)


def studen_info2(*args, **kwargs):  # args muestra como lista y kwargs como diccionrio
    print(args)
    print(kwargs)


cursos = ['Mate', 'Arte']
info = {'name': 'John', 'age': 22}

studen_info2(*cursos, **info)

"""


# Año bisiesto

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
print(days_in_month(2020, 2))
