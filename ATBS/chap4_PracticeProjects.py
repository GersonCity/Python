# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item
import copy
spam = ['apples', 'bananas', 'tofu', 'cats']


def commaCode(*formatLista):
    lista = copy.copy(formatLista)
    r = ', '.join(*formatLista)
    ultimoValor = 'and' + r.rsplit(',', 1)[1]
    # formatLista.insert(1, 'chicken')
    print(formatLista)
    # r_add = r.insert(-2, 'and')
    print(r)
    print(ultimoValor)


commaCode(spam)
