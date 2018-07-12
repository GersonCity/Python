# Funciones
# def hello():
#     print('Howdy!')
#     print('Howdy!!')
#     print('Howdy!!!')


# hello()


# def hola(name):
#     print('Hello' + name)


# hola('Alice')
# hola('Bob')

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)  # Almacenamos el valor random entre 1 y 9 que trae la funcion random.randint
# print(r)
fortune = getAnswer(r)  # le pasamos a variable fortune la funcion getAnswe con su parametro r obtenido de funcion randon.randint
print(fortune)

# tambien se puede simplificar las 3 lineas de arriba por solo 1
print(getAnswer(random.randint(1, 9)))


# None Value

spam = print('hello!')
None == spam

# print function
print('cats', 'dogs', 'mice')  # imprime separado por espacio
print('cats', 'dogs', 'mice', sep=',')  # imprime separado por una coma

# Local and Global Scope


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()
# When the program starts, the spam() function is called ❺, and a local scope is created. The local variable eggs ❶ is set to 99. Then the bacon() function is called ❷, and a second local scope is created. Multiple local scopes can exist at the same time. In this new local scope, the local variable ham is set to 101, and a local variable eggs—which is different from the one in spam()’s local scope—is also created ❹ and set to 0.

# When bacon() returns, the local scope for that call is destroyed. The program execution continues in the spam() function to print the value of eggs ❸, and since the local scope for the call to spam() still exists here, the eggs variable is set to 99. This is what the program prints.


# Global Variables Can Be Read from a Local Scope
def spam():
    print(eggs2)


eggs2 = 42  # variable global
spam()
print(eggs2)


# The global Statement
def spam():
    global huevo
    huevo = 'spam_huevo'


huevo = 'global_huevo'
spam()
print(huevo)

# ----------------------------------------


def spam():
    global eggs_
    eggs_ = 'spam_eggs_'  # this is the global


def bacon():
    eggs_ = 'bacon_eggs_'  # this is a local


def ham():
    print(eggs_)  # this is the global


eggs_ = 42  # this is the global
spam()
print(eggs_)


# Exception Handling
