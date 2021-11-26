import unittest
from unittest.mock import patch

from utils.utils import default_write_to_file
from constants.constants import test_txt_file_name, test_text_to_write


class TestDefaultWriteToFile(unittest.TestCase):
    test_file_name = test_txt_file_name
    text_to_write = test_text_to_write

    def setUp(self):
        self.default_write_to_file = default_write_to_file

    def test_default_write_to_file(self):
        self.default_write_to_file(self.test_file_name, self.text_to_write)

        file = open(self.test_file_name, 'r')
        text = file.read()

        self.assertEqual(text, self.text_to_write)

        file.close()

    @patch('builtins.print')
    def test_success_print(self, mock_print):
        self.default_write_to_file(self.test_file_name, self.text_to_write)
        mock_print.assert_called_with('Запись в файл прошла успешно.')


if __name__ == "__main__":
    unittest.main()
