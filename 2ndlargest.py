count = 0

largest = float("-inf")
second_largest = float("-inf")
smallest = float("+inf")

while count < 5:
    num = int(input("Give me a number "))
    if num > largest:
        second_largest = largest
        largest = num
    elif (num > second_largest < largest):
        second_largest = num
    if (num < smallest):
        smallest = num;

    count = count + 1

print("the largest number is ", largest)

print("the second largest number is ", second_largest)
print("the smallest number is ", smallest)