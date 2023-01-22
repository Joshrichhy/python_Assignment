import unittest

from Class_Practice.Animal import Animal


class TestAnimalClass(unittest.TestCase):

    animal = Animal("Snoop", "Yoruba", "100 mile", True)

    def test_animal_name(self):
        # given
        self.animal.set__animal_name("Snoop")
        # when
        result = self.animal.get_animal_name()
        # assert
        self.assertEqual("Snoop", result)

    def test_animal_speak(self):
        self.animal.set_animal_speak("Yoruba")
        language = self.animal.get_speak()
        self.assertEqual("Yoruba", language)

    def test_animal_dance(self):
        self.animal.set_animal_dance("Shoki")
        dance_Move = self.animal.get_dance()
        self.assertEqual("Shoki", dance_Move)

    def test_can_run(self):
        self.animal.set_run(True)
        c = self.animal.can_run()
        self.assertTrue(c)

    def test_animal_has_list(self):
        self.animal.set_food("fries", "eba", "Jelof")
        f = self.animal.get_food()
        self.assertEquals(["fries", "eba", "Jelof"], f)


