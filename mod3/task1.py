import unittest
from freezegun import freeze_time
import datetime

def get_username(greeting):
    weekday = datetime.datetime.now().strftime('%A')
    return f'{greeting} {weekday}'

class GreetingTest(unittest.TestCase):

    @freeze_time("2025-04-14")
    def test_correct_weekday_in_username(self):
        expected = "Хорошего дня Monday"
        result = get_username("Хорошего дня")
        self.assertEqual(result, expected)

    @freeze_time("2025-04-16")
    def test_custom_input_username_contains_weekday(self):
        result = get_username("Хорошего дня")
        self.assertIn("Wednesday", result)  # Direct check for Wednesday