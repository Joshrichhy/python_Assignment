def add_even(card):
    total_sum_of_even_digit_number = 0
    for number in range(len(card) - 2, -1, -2):
        sum_of_even_digit = (int(card[number]) * 2)
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


class Credit_card_validator:

    def __init__(self, card_sum, card_validation, card_type):
        self.card_type = card_type
        self.card_validation = card_validation
        self.card_sum = card_sum

    def set_sum(self, card):
        self.card_sum = add_even(card) + add_odd_numbers(card)

    def set_card_validation(self, card):
        self.card_validation = self.card_length_validity(card)

    def get_card_validation(self):
        return self.card_validation

    def get_card_sum(self):
        return self.card_sum

    def set_card_type(self, card_number):
        if card_number.startswith("4"):
            self.card_type = "VisaCard"
        elif card_number.startswith("5"):
            self.card_type = "MasterCard"
        elif card_number.startswith("37"):
            self.card_type = "American Express Cards"
        elif card_number.startswith("6"):
            self.card_type = "DiscoverCard"
        else:
            self.card_type = "Invalid card type"

    def get_card_type(self):
        return self.card_type

    def card_length_validity(self, card_number):
        if len(card_number) < 13 or len(card_number) > 16:
            return "invalid"
        else:
            return "valid"

    def check_card_validation(self, card_number):
        self.set_sum(card_number)
        if self.get_card_sum() % 10 == 0:
            print("****Card Type: valid")
            return "valid"
        else:
            print("****Card Type Validity: invalid")
            return "invalid"
