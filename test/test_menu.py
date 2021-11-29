import unittest
from unittest.mock import patch

from core.menu import Menu
from constants.constants import print_wrong_item


class TestMenu(unittest.TestCase):
    test_number1 = '1'
    test_number2 = '2'
    test_number3 = '3'
    menu_test_text = 'test text for input'

    def setUp(self):
        self.menu = Menu(self.menu_test_text)
        self.test_menu_modes = {
            self.test_number1: self.test1,
            self.test_number2: self.test2,
            self.test_number3: self.test3,
        }
        self.counter = 0

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

    @patch('core.menu.Menu.checkout_number')
    @patch('builtins.input')
    def test_run_menu(self, mock_input, mock_checkout_number):
        self.menu.run_menu(self.test_menu_modes)

        self.assertTrue(mock_checkout_number.called)
        mock_input.assert_called_with(self.menu_test_text)

    @patch('builtins.input')
    def test_get_menu_number(self, mock_input):
        self.menu.get_menu_number()
        mock_input.assert_called_with(self.menu_test_text)

    @patch('core.menu.Menu.run_menu')
    @patch('builtins.print')
    def test_false_get_menu_number(self, mock_print, mock_run_menu):
        self.menu.checkout_number('4', self.test_menu_modes)

        mock_run_menu.assert_called_with(self.test_menu_modes)
        self.assertTrue(mock_run_menu.called)
        mock_print.assert_called_with(print_wrong_item)


if __name__ == "__main__":
    unittest.main()
