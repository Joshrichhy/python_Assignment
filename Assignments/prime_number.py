user_input = int(input("Enter Number: "))
count = 2

while count <= user_input:
    if user_input % count != 0:
        print(user_input, "is a prime number")
    else:
        print(user_input, "is not a prime number")
    break