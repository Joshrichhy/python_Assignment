number = 65
guess = int(input("guess a number: "))
count = 0

while count < 5:
    if guess == number:
        print(" you got it baba")
        break

    else:
        count += 1
        if guess != number:
            print("try again later: ")
            int(input("guess a number: "))

print("the number you could not get is  ", number)
