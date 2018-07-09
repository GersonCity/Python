print('Importando my_module...')

test = 'Test String'


def find_index(to_search, target):
    ''' Encuentra el index de un valor en una secuencia'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
