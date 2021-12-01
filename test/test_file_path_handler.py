import unittest
from unittest.mock import patch

from core.menu import Menu
from core.custom_error import CustomError
from core.file_path_handler import FilePathHandler
from constants.constants import input_file_path, print_wrong_path, print_wrong_extension, default_menu_text
from test.constants.constatns import test_jp, test_csv, test_txt, test_menu_modes, builtins_print, builtins_input, \
    path_of_check_file, path_of_handler_wrong_path, path_of_run_menu


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.FilePathHandler = FilePathHandler()

    @patch(path_of_check_file)
    @patch(builtins_input)
    def test_get_file_path(self, mock_input, mock_check_file):
        self.FilePathHandler.get_file_path()

        self.assertTrue(mock_check_file.called)
        mock_check_file.assert_called_with(input(input_file_path))
        mock_input.assert_called_with(input_file_path)

    def test_check_file(self):
        self.assertEqual(self.FilePathHandler.check_file(test_txt), test_txt)

    @patch(builtins_print)
    def test_false_check_file(self, *args):
        self.assertIsNone(self.FilePathHandler.check_file(test_csv))

    def test_check_file_is_exist(self):
        self.FilePathHandler.check_file_is_exist(test_txt)

    def test_check_file_extension(self):
        self.FilePathHandler.check_file_extension(test_txt)

    def test_false_check_file_is_exist(self):
        with self.assertRaises(CustomError) as context:
            self.FilePathHandler.check_file_is_exist(test_csv)

        self.assertEqual(context.exception.text, print_wrong_path)

    def test_false_check_file_extension(self):
        with self.assertRaises(CustomError) as context:
            self.FilePathHandler.check_file_extension(test_jp)

        self.assertEqual(context.exception.text, print_wrong_extension)


if __name__ == '__main__':
    unittest.main()
