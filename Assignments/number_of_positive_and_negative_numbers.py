negative_counter = 0
positive_counter = 0
sum = 0
count = 1

user_Input = int(input("Enter number and enter 0 to terminate: "))
while user_Input != 0:
    if user_Input > 0:
        positive_counter += 1
    elif user_Input < 0:
        negative_counter += 1

    sum += user_Input
    average = sum / count
    count += 1
    user_Input = int(input("Enter number and enter 0 to terminate: "))
if sum == 0:
    print("no number was entered except 0")
else:
    print("The numbers of positives is ", positive_counter, "\nThe numbers of negatives is ", negative_counter)
    print("The total is ", sum,  "\nThe average is ", average)
