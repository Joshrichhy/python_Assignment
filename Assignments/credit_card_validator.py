card_details = input("Enter Card Details: ")
print("*************************************")

print("****Card Number: ", card_details)


def card_validate(card_number)    if len(card_number) <= 13 or len(card_number) > 16:
        return "invalid"
    else:
        return "Valid"


def add_even(card_number):
    total_sum_of_even_digit_number = 0
    for number in range(len(card_number) - 2, -1, -2):
        sum_of_even_digit = (int(card_number[number]) * 2)
        if sum_of_even_digit > 9:
            newSum = (sum_of_even_digit % 10) + (sum_of_even_digit // 10)
            total_sum_of_even_digit_number += newSum
        else:
            total_sum_of_even_digit_number += sum_of_even_digit
    return total_sum_of_even_digit_number


def add_odd_numbers(card_number):
    sum_of_odd_digit = 0
    for i in range(len(card_number) - 1, -1, -2):
        sum_of_odd_digit += int(card_number[i])
    return sum_of_odd_digit


print("****Card length Validity: ", card_validate(card_details))
print("****Card Length: ", len(card_details))

sum_of_numbers_in_card = add_even(card_details) + add_odd_numbers(card_details)
if (sum_of_numbers_in_card % 10) == 0:
    print("****Card Type: valid")
else:
    print("****Card Type: invalid")


def card_type(card_number):
    if card_number[0] == "4":
        return "VisaCard"
    elif card_number[0] == "5":
        return "MasterCard"
    elif card_number[0] == "3" and card_number[1] == "7":
        return "American Express Cards"
    elif card_number[0] == "6":
        return "DiscoverCard"
    else:
        return "Invalid card type"


print("****Card Type: ", card_type(card_details))
print("*************************************")
