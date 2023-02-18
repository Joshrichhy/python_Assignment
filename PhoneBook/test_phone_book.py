from unittest import TestCase

from PhoneBook.phone_book import phonebook


class Test(TestCase):
    my_phonebook = phonebook()
    my_phonebook.create_contact("Joshua", "Kuse", "07033490197", "kuse@gmail.com")

    def test_create_contact(self):

        self.assertEqual(1, self.my_phonebook.count_contact())

    def test_contact_can_be_viewed(self):
        self.my_phonebook.create_contact("Josh", "Kuse", "07033490197", "kuse@gmail.com")

        expected = """
       Contact Name: Josh Kuse
       Contact Phone Number: 07033490197
       Contact Email-Address: kuse@gmail.com
       """
        self.assertEqual(expected,  self.my_phonebook.view_contact("Josh Kuse"))

    def test_that_contact_can_be_edited(self):
        self.my_phonebook.edit_contact("Joshua Kuse", "Spencer", "Yinka", "080", "sy")
        expected = """
       Contact Name: Spencer Yinka
       Contact Phone Number: 080
       Contact Email-Address: sy
       """
        self.assertEqual(expected, self.my_phonebook.view_contact("Spencer Yinka"))

    def test_contact_can_be_deleted(self):
        self.my_phonebook.create_contact("Josh", "Kuse", "07033490197", "kuse@gmail.com")
        self.my_phonebook.delete_contact("Josh Kuse")
        self.assertEqual(1, self.my_phonebook.count_contact())

   # def test_all_contact_can_be_viewed(self):
        #self.my_phonebook.edit_contact("Joshua Kuse", "Spencer", "Yinka", "080", "")
        #self.my_phonebook.create_contact("Josh", "Kuse", "07033490197", "kuse@gmail.com")

        #self.my_phonebook.view_all_contact()




