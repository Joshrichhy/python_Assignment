from unittest import TestCase

from Assignments.credit_card_validator.credit_card_validator import Credit_card_validator


class Test(TestCase):
    card_checker = Credit_card_validator(5, card_validation="valid", card_type="Master")

    def test_card_length_validity(self):
        # check if card length is between 13 and 16
        confirm_card_length = self.card_checker.card_length_validity("3433456754365776")
        # assert
        self.assertEqual("valid", confirm_card_length)

    def test_card_validity(self):
        confirm_card_validity = self.card_checker.check_card_validation("4388576018410707")
        self.assertEqual("valid", confirm_card_validity)

    def test_card_type(self):
        self.card_checker.set_card_type("4388576018410707")
        self.assertEqual("VisaCard", self.card_checker.get_card_type())

