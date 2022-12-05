import random

number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number "))
number_of_guesses = 0

while number_of_guesses < 3:
    if guess == number_to_be_guessed:
        print("you got it right")
        break
    else:
        if guess < number_to_be_guessed:
            print("number is lesser, Try again later")
        elif guess > number_to_be_guessed:
            print("number is greater")
        guess = int(input("Guess a number "))
    number_of_guesses += 1
if number_to_be_guessed != guess:
    print("it is a pity, the number you tried to guess since is ", number_to_be_guessed)


