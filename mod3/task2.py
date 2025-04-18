import unittest

from your_decrypt_module import decrypt  # или вставь сюда саму функцию

class DecryptTestCase(unittest.TestCase):
    def test_cases_with_no_dots(self):
        self.assertEqual(decrypt("абра-кадабра"), "абра-кадабра")

    def test_cases_with_simple_backspace(self):
        self.assertEqual(decrypt("абраа..-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абраа..-.кадабра"), "абра-кадабра")

    def test_cases_with_multiple_backspaces(self):
        self.assertEqual(decrypt("абра--..кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абрау...-кадабра"), "абра-кадабра")
        self.assertEqual(decrypt("абра........"), "")

    def test_mixed_symbols(self):
        self.assertEqual(decrypt("абр......a."), "")
        self.assertEqual(decrypt("1..2.3"), "23")

    def test_edge_cases(self):
        self.assertEqual(decrypt("."), "")
        self.assertEqual(decrypt("1......................."), "")

if __name__ == '__main__':
    unittest.main()
