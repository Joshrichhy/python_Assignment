from Assignments.credit_card_validator.credit_card_validator import Credit_card_validator

if __name__ == '__main__':
    card_checker = Credit_card_validator(5, card_validation="valid", card_type="Master")

    card_detail = input("Enter Card Details: ")
    print("*************************************")
    print("****Card Number: ", card_detail)
    card_checker.set_sum(card_detail)
    card_checker.set_card_validation(card_detail)
    card_checker.set_card_type(card_detail)

    print("****Card length Validity: ", card_checker.get_card_validation())
    print("****Card Length: ", len(card_detail))
    if card_checker.get_card_sum() % 10 == 0:
        print("****Card Type: valid")
    else:
        print("****Card Type Validity: invalid")

    print("****Card Type: ", card_checker.get_card_type())
    print("*************************************")
