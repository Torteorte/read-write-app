import unittest
from unittest.mock import patch

from core.menu import Menu


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

    @patch('builtins.input')
    def test_run_menu(self, mock_input):
        patcher = patch.object(Menu, 'checkout_number')
        patched = patcher.start()

        self.menu.run_menu(self.test_menu_modes)
        assert patched.call_count == 1

        patched.assert_called_with(self.menu.get_menu_number(), self.test_menu_modes)
        mock_input.assert_called_with(self.menu_test_text)
        patcher.stop()

    @patch('builtins.input')
    def test_get_menu_number(self, mock_input):
        self.menu.get_menu_number()
        mock_input.assert_called_with(self.menu_test_text)

    @patch('builtins.print')
    def test_false_get_menu_number(self, mock_print):
        patcher = patch.object(Menu, 'run_menu')
        patched = patcher.start()

        self.menu.checkout_number('4', self.test_menu_modes)
        assert patched.call_count == 1

        patched.assert_called_with(self.test_menu_modes)
        mock_print.assert_called_with('Такого пункта нет.')
        patcher.stop()


if __name__ == "__main__":
    unittest.main()
