count = 1
counter = 0
user_input = int(input("Enter Number: "))

while (count <= user_input):
        if (user_input % count == 0):
            counter += 1
        count += 1
print(user_input, "has", counter, "factors")
