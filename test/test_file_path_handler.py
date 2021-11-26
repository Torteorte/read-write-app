import unittest
from unittest.mock import patch

from core.file_path_handler import FilePathHandler
from constants.constants import test_txt, test_csv, test_jp, input_file_path, print_wrong_path, print_wrong_extension


class TestFileHandler(unittest.TestCase):
    test_txt = test_txt
    test_csv = test_csv
    test_jp = test_jp

    def setUp(self):
        self.FilePathHandler = FilePathHandler('', '')
        open(self.test_txt, 'w').close()

    def test_check_file_status(self):
        self.assertRaises(TypeError, self.FilePathHandler.check_file_status(self.test_txt))

    def test_valid_check_file_extension(self):
        self.assertRaises(TypeError, self.FilePathHandler.check_file_extension(self.test_txt))
        self.assertRaises(TypeError, self.FilePathHandler.check_file_extension(self.test_csv))

    @patch('builtins.print')
    def test_invalid_check_file_status(self, mock_print):
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_status(self.test_csv)

        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_status(self.test_jp)

        mock_print.assert_called_with(print_wrong_path)

    @patch('builtins.print')
    def test_invalid_check_file_extension(self, mock_print):
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_extension(self.test_jp)

        mock_print.assert_called_with(print_wrong_extension)

    def test_check_file(self):
        self.assertEqual(self.FilePathHandler.check_file(self.test_txt), self.test_txt)

    @patch('builtins.print')
    def test_invalid_file_path(self, mock_print):
        patcher = patch.object(FilePathHandler, 'handler_wrong_path')
        patched = patcher.start()

        self.FilePathHandler.check_file(self.test_jp)
        assert patched.call_count == 1

        patched.assert_called_with()
        mock_print.assert_called_with(print_wrong_path)

        patcher.stop()

    @patch('builtins.input')
    def test_get_file_path(self, mock_input):
        patcher = patch.object(FilePathHandler, 'check_file')
        patched = patcher.start()

        self.FilePathHandler.get_file_path()
        assert patched.call_count == 1

        patched.assert_called_with(input(input_file_path))
        mock_input.assert_called_with(input_file_path)

        patcher.stop()


if __name__ == '__main__':
    unittest.main()
