import unittest
from unittest.mock import patch

from core.menu import Menu
from constants.constants import print_wrong_item, menu_test_text
from test.utils.utils import test_function_one, test_function_two
from test.constants.constatns import test_number1, test_number2, test_menu_modes, builtins_input, builtins_print, \
    path_of_checkout_number, path_of_run_menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu(menu_test_text, test_menu_modes)

    @patch(path_of_checkout_number)
    @patch(builtins_input)
    def test_run_menu(self, mock_input, mock_checkout_number):
        self.menu.run_menu()

        self.assertIsNotNone(self.menu._menu_modes)
        self.assertTrue(mock_checkout_number.called)
        mock_input.assert_called_with(menu_test_text)

    @patch(path_of_checkout_number)
    @patch(builtins_input)
    def test_menu_modes_is_none(self, *args):
        menu_none_mods = Menu(menu_test_text, test_menu_modes)
        menu_none_mods.run_menu()

        self.assertIsNotNone(menu_none_mods._menu_modes)

    @patch(builtins_input)
    def test_get_menu_number(self, mock_input):
        self.menu.get_menu_number()
        mock_input.assert_called_with(menu_test_text)

    def test_checkout_number_function_one(self):
        self.assertEqual(self.menu.checkout_number(test_number1), test_function_one())
        self.assertEqual(self.menu.checkout_number(test_number1), 1)

    def test_checkout_number_function_two(self):
        self.assertEqual(self.menu.checkout_number(test_number2), test_function_two())
        self.assertEqual(self.menu.checkout_number(test_number2), 2)

    @patch(path_of_run_menu)
    @patch(builtins_print)
    def test_false_checkout_number(self, mock_print, mock_run_menu):
        self.menu.checkout_number('4')

        self.assertTrue(mock_run_menu.called)
        mock_print.assert_called_with(print_wrong_item)


if __name__ == "__main__":
    unittest.main()
