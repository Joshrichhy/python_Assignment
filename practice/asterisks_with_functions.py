asterisks = int(input("Enter Number of Asterisks: "))


def asterisks_right(input):
    for i in range(1, input, 2):
        i = i * '*'
        print(i)


asterisks_right(asterisks)

asterisks = int(input("Enter Number of Asterisks: "))


def asterisks_left(input):
    for i in range(input, 0, -2):
        aster = i * '*'
        print(aster.center(i))


def asterisks_middle(input):
    for i in range(-1, input, 2):
        aster = i * '*'
        print(aster.center(input))
    for j in range(input, -1, -2):
        star = j * '*'
        print(star.center(input))


asterisks_middle(asterisks)


def square_with_asterisks(user_input):
    for i in range(user_input, 0, -1):
        square = user_input * '*'
        print(square)


asterisk = int(input("Enter Number of Asterisks: "))
square_with_asterisks(asterisk)
