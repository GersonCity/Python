
# The Collatz Sequence


def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


while True:
    try:
        print('Type a Number: ')
        guess = int(input())

        # guess = 3
        num = collatz(guess)
        print(num)

        while num != 1:
            if num == 1:
                break
            else:
                num = collatz(num)
                print(num)
                continue

    except ValueError:
        print('Error! Debe ingresar un numero')
