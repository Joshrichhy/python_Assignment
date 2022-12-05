number = int(input("Enter Number: "))
factor = 1
sum = 0
while factor < number:
    if number % factor == 0:
        sum  = sum + factor
        print(factor, end=' ')
    factor +=1
print("=", sum)
if sum == number:
    print("number is perfect")
elif sum > number:
    print("number is abundant")
else:
    sum < number
    print("number is deficient")

