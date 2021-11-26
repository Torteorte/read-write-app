import os
import unittest
from unittest.mock import patch

from core.file_Handler_abc import FileHandlerABC, CSVFileHandler, TXTFileHandler
from constants.constants import csv_test_text_to_write, test_csv_file_name, csv_result_text, test_text_to_write, \
    test_txt_file_name, test_txt_file_empty, print_empty_file, print_success_write


class TestCSVFileHandler(unittest.TestCase):
    csv_file = test_csv_file_name
    csv_result_text = csv_result_text
    csv_text_to_write = csv_test_text_to_write

    txt_file = test_txt_file_name
    txt_text_to_write = test_text_to_write

    empty_txt_file = test_txt_file_empty

    def setUp(self):
        self.CSVFileHandler = CSVFileHandler(self.csv_file)
        self.TXTFileHandler = TXTFileHandler(self.txt_file)
        self.TXT_empty = TXTFileHandler(self.empty_txt_file)

    @patch("core.file_Handler_abc.FileHandlerABC.__abstractmethods__", set())
    def test_write_to_file(self):
        file_handler_abc = FileHandlerABC('')
        self.assertIsNone(file_handler_abc.write_to_file(''))

    @patch('builtins.print')
    def test_read_file(self, mock_print):
        self.TXTFileHandler.read_file()
        mock_print.assert_called_with(self.txt_text_to_write)

    @patch('builtins.print')
    def test_read_empty_file(self, mock_print):
        self.TXT_empty.read_file()
        mock_print.assert_called_with(print_empty_file)

    @patch('builtins.print')
    def test_csv_write_to_file(self, mock_print):
        self.CSVFileHandler.write_to_file(self.csv_text_to_write)

        file = open(self.csv_file, 'r')
        text = file.read()

        self.assertEqual(text, self.csv_result_text)

        file.close()
        os.remove(self.csv_file)

        mock_print.assert_called_with(print_success_write)


if __name__ == "__main__":
    unittest.main()
