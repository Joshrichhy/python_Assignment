number = 65
count = 0

while count < 5:
    guess = int(input("guess a number: "))
    if guess == number:
        print(" you got it baba")

        break

    else:
        if guess != number:
            print("try again later: ")
    count += 1

if guess != number:
    print("the number you could not get is  ", number)
