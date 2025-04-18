import unittest
import datetime  # Import datetime to get the current year
from person import Person

class PersonTest(unittest.TestCase):

    def setUp(self):
        self.person = Person("Иван", 1990)

    def test_get_age(self):
        expected_age = datetime.datetime.now().year - 1990  # Dynamically calculate age
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "Иван")

    def test_set_name(self):
        self.person.set_name("Пётр")
        self.assertEqual(self.person.get_name(), "Пётр")

    def test_set_address(self):
        self.person.set_address("Москва")
        self.assertEqual(self.person.get_address(), "Москва")

    def test_is_homeless_true(self):
        self.assertTrue(self.person.is_homeless())

    def test_is_homeless_false(self):
        self.person.set_address("Новосибирск")
        self.assertFalse(self.person.is_homeless())

if __name__ == '__main__':
    unittest.main()