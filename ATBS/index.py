
# print('Hola mundo')
# print('Cual es tu nombre?')
# myName = input()
# print('Es bueno conocerte, ' + myName)
# print('El largo de tu nombre es:')
# print(len(myName))
# print('Cual es tu Edad?')
# myAge = input()
# print('Tu tendras ' + str(int(myAge) + 1) + ' en un año mas.')


while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)')
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)
()
