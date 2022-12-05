odd_number_counter = 0
even_number_counter = 0
sum_odd = 0
sum_even = 0

user_input = int(input("Enter Number or any Negative number to quit: "))

while user_input > 0:
    if user_input % 2 == 0:
        sum_even += user_input
        even_number_counter += 1

    else:
        if user_input % 2 != 0:
            sum_odd += user_input
            odd_number_counter += 1

    user_input = int(input("Enter Number or any Negative number to quit: "))


print("number of even number is ", even_number_counter)
print("number of odd number is ", odd_number_counter)
print("sum of even number is ", sum_even)
print("sum of odd number is ", sum_odd)
