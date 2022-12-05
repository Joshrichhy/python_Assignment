count = 0

largest = float("-inf")
smallest = float("+inf")

while count < 5:
    num = int(input("Give me a number "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    count = count + 1

if largest > smallest:
    print("the largest number is ", largest)
if smallest < largest:
    print("the smallest number is ", smallest)

