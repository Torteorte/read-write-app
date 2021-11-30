import unittest
from unittest.mock import patch

from utils.utils import default_write_to_file
from constants.constants import print_success_write
from test.constants.constatns import test_txt_file_name, test_text_to_write


class TestDefaultWriteToFile(unittest.TestCase):
    test_file = test_txt_file_name
    text_to_write = test_text_to_write

    @patch('builtins.print')
    def test_default_write_to_file(self, mock_print):
        default_write_to_file(self.test_file, self.text_to_write)

        file = open(self.test_file, 'r')
        text = file.read()

        self.assertEqual(text, self.text_to_write)
        mock_print.assert_called_with(print_success_write)

        file.close()


if __name__ == "__main__":
    unittest.main()

