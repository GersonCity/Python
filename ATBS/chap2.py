# print('Hola mundo')
# print('Cual es tu nombre?')
# myName = input()
# print('Es bueno conocerte, ' + myName)
# print('El largo de tu nombre es:')
# print(len(myName))
# print('Cual es tu Edad?')
# myAge = input()
# print('Tu tendras ' + str(int(myAge) + 1) + ' en un año mas.')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':  # (1)
#         continue  # (2)
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()  # (3)
#     if password == 'swordfish':
#         break  # (4)
# print('Access granted.')  # (5)


# name = ''
# while not name:  # (1)
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:  # (2)
#     print('Be sure to have enough room for all your guests.')  # (3)
# print('Done')

# # If the user enters a blank string for name, then the while statement’s condition will be True ❶, and the program continues to ask for a name. If the value for numOfGuests is not 0 ❷, then the condition is considered to be True, and the program will print a reminder for the user ❸.

# 9
# spam = 1
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('howdy')
# else:
#     print('greetings!')

# 13
for i in range(1, 11):
    print(i)
    # i = i + 1 NO ES NECESARIO AGREGAR UN INCREMENTO

# x = 1
# while x <= 10:
#     print(x)
#     x = x + 1
