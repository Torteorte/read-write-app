import unittest
from unittest.mock import patch

from core.menu import Menu
from core.custom_error import CustomError
from core.file_path_handler import FilePathHandler

from constants.constants import input_file_path, print_wrong_path, print_wrong_extension, default_menu_text
from test.constants.constatns import test_jp, test_csv, test_txt, test_menu_modes


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.menu = Menu(default_menu_text, test_menu_modes)
        self.FilePathHandler = FilePathHandler(self.menu)

    @patch('core.file_path_handler.FilePathHandler.check_file')
    @patch('builtins.input')
    def test_get_file_path(self, mock_input, mock_check_file):
        self.FilePathHandler.get_file_path()

        self.assertTrue(mock_check_file.called)
        mock_check_file.assert_called_with(input(input_file_path))
        mock_input.assert_called_with(input_file_path)

    def test_check_file(self):
        self.assertEqual(self.FilePathHandler.check_file(test_txt), test_txt)

    @patch('builtins.print')
    @patch('core.file_path_handler.FilePathHandler.handler_wrong_path')
    def test_false_check_file(self, mock_handler_wrong_path, *args):
        self.FilePathHandler.check_file(test_csv)

        self.assertTrue(mock_handler_wrong_path.called)

    def test_check_file_is_exist(self):
        try:
            self.FilePathHandler.check_file_is_exist(test_txt)
        except CustomError:
            self.fail("Unexpected raise!")

    def test_check_file_extension(self):
        try:
            self.FilePathHandler.check_file_extension(test_txt)
        except CustomError:
            self.fail("Unexpected raise!")

    def test_false_check_file_is_exist(self):
        with self.assertRaises(CustomError) as context:
            self.FilePathHandler.check_file_is_exist(test_csv)

        self.assertEqual(context.exception.text, print_wrong_path)

    def test_false_check_file_extension(self):
        with self.assertRaises(CustomError) as context:
            self.FilePathHandler.check_file_extension(test_jp)

        self.assertEqual(context.exception.text, print_wrong_extension)

    @patch('core.menu.Menu.run_menu')
    def test_handler_wrong_path(self, mock_run_menu):
        self.FilePathHandler.handler_wrong_path()
        self.assertTrue(mock_run_menu.called)


if __name__ == '__main__':
    unittest.main()
