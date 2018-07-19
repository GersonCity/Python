
nums = [1, 2, 3, 4, 5]

# Si encuentra el numero sale del loop
for num in nums:
    if num == 3:
        print(str(num) + ' ' + 'Found!')
        break
    print(num)

# # Si encuentra numero, imprime y continua con los demas numeros
for num in nums:
    if num == 3:
        print(str(num) + ' ' + 'Found!')
        continue
    print(num)

# loop dentro de otro loop, el siguiente loop nos todas las posibles combinaciones
for num in nums:
    for letter in 'abc':
        print(num, letter)

# imprime del 1 al 10
for i in range(1, 11):
    print(i)

# while loop
 x = 0

# while x < 10:
#     print(x)
#     x += 1

# loop infinito   CNTRL + pause(-) para cancelar
 while True:
     print(x)
     x += 1



