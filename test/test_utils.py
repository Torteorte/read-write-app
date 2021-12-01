import unittest
from unittest.mock import patch

from utils.utils import default_write_to_file, get_file_extension
from constants.constants import print_success_write
from test.constants.constatns import test_txt_file_name, test_text_to_write


class TestDefaultWriteToFile(unittest.TestCase):

    @patch('builtins.print')
    def test_default_write_to_file(self, mock_print):
        default_write_to_file(test_txt_file_name, test_text_to_write)

        file = open(test_txt_file_name, 'r')

        self.assertEqual(file.read(), test_text_to_write)
        mock_print.assert_called_with(print_success_write)

        file.close()

    # def test_get_file_extension(self):
    #     self.assertEqual(get_file_extension(test_txt_file_name), '.txt')


if __name__ == "__main__":
    unittest.main()

