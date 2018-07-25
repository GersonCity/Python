# Strings

print("Hello there!\nHow are you?\nI\'m doing fine.")
print(r'That is Carol\'s cat.')  # el backslash se considera en el string

# 1
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
# 2
print('Dear Alice, \n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely, \nBob')

"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""


def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

# Indexing and Slicing Strings


spam = 'Hello world!'
print(spam[0])

spam = 'Hello world!'
fizz = spam[0:5]
print(fizz)


# Useful String Methods
# The upper(), lower(), isupper(), and islower() String Methods

spam = 'Hello world!'
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())

# The isX String Methods
# The isX string methods are helpful when you need to validate user input
'''

    isalpha() returns True if the string consists only of letters and is not blank.

    isalnum() returns True if the string consists only of letters and numbers and is not blank.

    isdecimal() returns True if the string consists only of numeric characters and is not blank.

    isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.

    istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

'''

print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('    '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())


# Ejemplo :
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')


# The startswith() and endswith() String Methods
'Hello world!'.startswith('Hello')
True
>> > 'Hello world!'.endswith('world!')
True
>> > 'abc123'.startswith('abcdef')
False
>> > 'abc123'.endswith('12')
False
>> > 'Hello world!'.startswith('Hello world!')
True
>> > 'Hello world!'.endswith('Hello world!')
True


# The join() and split() String Methods
# JOIN llama a una valor string y pasa una lista // split llama a un string y retorna una lista de strings

print(', '.join(['cats', 'rats', 'bats']))
# 'cats, rats, bats'
print(' '.join(['My', 'name', 'is', 'Simon']))
#'My name is Simon'
print('ABC'.join(['My', 'name', 'is', 'Simon']))
# 'MyABCnameABCisABCSimon'

print('My name is Simon'.split())
# ['My', 'name', 'is', 'Simon']
print('MyABCnameABCisABCSimon'.split('ABC'))
# ['My', 'name', 'is', 'Simon']
print('My name is Simon'.split('m'))
# ['My na', 'e is Si', 'on']


spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')
'''['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.',
'Sincerely,', 'Bob'] '''


# Justifying Text with rjust(), ljust(), and center()
>> > 'Hello'.rjust(10)
'     Hello'
>> > 'Hello'.rjust(20)
'               Hello'
>> > 'Hello World'.rjust(20)
'         Hello World'
>> > 'Hello'.ljust(10)
'Hello     '

>> > 'Hello'.rjust(20, '*')
'***************Hello'
>> > 'Hello'.ljust(20, '-')
'Hello---------------'

>> > 'Hello'.center(20)
'       Hello       '
>> > 'Hello'.center(20, '=')
'=======Hello========'

# Ejemplo :


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

'''
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000

'''

# Removing Whitespace with strip(), rstrip(), and lstrip()
>> > spam = '    Hello World     '
>> > spam.strip()
'Hello World'
>> > spam.lstrip()
'Hello World '
>> > spam.rstrip()
'    Hello World'

>> > spam = 'SpamSpamBaconSpamEggsSpamSpam'
>> > spam.strip('ampS')
'BaconSpamEggs'

# Copying and Pasting Strings with the pyperclip Module
>> > import pyperclip
>> > pyperclip.copy('Hello world!')
>> > pyperclip.paste()
'Hello world!'
