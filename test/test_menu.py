import unittest
from core.menu import Menu


class TestMenu(unittest.TestCase):
    test_number1 = '1'
    test_number2 = '2'
    test_number3 = '3'

    def setUp(self):
        self.menu = Menu('test text')
        self.test_menu_modes = {
            self.test_number1: self.test1,
            self.test_number2: self.test2,
            self.test_number3: self.test3,
        }

    def test1(self):
        return 1

    def test2(self):
        return 2

    def test3(self):
        return 3

    def test_checkout_number(self):
        self.assertEqual(self.menu.checkout_number(self.test_number1, self.test_menu_modes), self.test1())
        self.assertEqual(self.menu.checkout_number(self.test_number2, self.test_menu_modes), self.test2())
        self.assertNotEqual(self.menu.checkout_number(self.test_number3, self.test_menu_modes), self.test1())


if __name__ == "__main__":
    unittest.main()
