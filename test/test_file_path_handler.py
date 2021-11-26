import unittest
from unittest.mock import patch

from core.file_path_handler import FilePathHandler


class TestFileHandler(unittest.TestCase):
    test_txt = 'text_files/some_test.txt'
    test_csv = 'mythic.csv'
    test_jp = 'test.木'

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

        mock_print.assert_called_with('Такого файла или пути не существует')

    @patch('builtins.print')
    def test_invalid_check_file_extension(self, mock_print):
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_extension(self.test_jp)

        mock_print.assert_called_with('Неверное расширение файла. Валидные расширения .csv, .txt, .doc')

    def test_check_file(self):
        self.assertEqual(self.FilePathHandler.check_file(self.test_txt), self.test_txt)

    @patch('builtins.print')
    def test_invalid_file_path(self, mock_print):
        patcher = patch.object(FilePathHandler, 'handler_wrong_path')
        patched = patcher.start()

        self.FilePathHandler.check_file(self.test_jp)
        assert patched.call_count == 1

        patched.assert_called_with()
        mock_print.assert_called_with('Такого файла или пути не существует')

        patcher.stop()


    @patch('builtins.input')
    def test_get_file_path(self, mock_input):
        patcher = patch.object(FilePathHandler, 'check_file')
        patched = patcher.start()

        self.FilePathHandler.get_file_path()
        assert patched.call_count == 1

        patched.assert_called_with(input('Путь к файлу: '))
        mock_input('Путь к файлу: ')

        patcher.stop()


if __name__ == '__main__':
    unittest.main()
