import os
import unittest
from unittest.mock import patch

from core.file_handler_abc import FileHandlerABC, CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import print_empty_file, print_success_write
from test.constants.constatns import test_csv_file_name, test_txt_file_name, test_doc_file_name, test_txt_file_empty, \
    test_text_to_write, csv_test_text_to_write, csv_result_text


class TestFileHandlerABC(unittest.TestCase):
    csv_file = test_csv_file_name
    csv_result_text = csv_result_text
    csv_text_to_write = csv_test_text_to_write

    txt_file = test_txt_file_name
    txt_text_to_write = test_text_to_write

    empty_txt_file = test_txt_file_empty
    doc_file = test_doc_file_name

    def setUp(self):
        self.csv_file_handler = CSVFileHandler(self.csv_file)
        self.txt_file_handler = TXTFileHandler(self.txt_file)
        self.doc_file_handler = DOCFileHandler(self.doc_file)
        self.txt_empty = TXTFileHandler(self.empty_txt_file)

    @patch("core.file_handler_abc.FileHandlerABC.__abstractmethods__", set())
    def test_write_to_file(self):
        file_handler_abc = FileHandlerABC('')
        self.assertIsNone(file_handler_abc.write_to_file(''))

    @patch('builtins.print')
    def test_read_file(self, mock_print):
        self.txt_file_handler.write_to_file(self.txt_text_to_write)
        self.txt_file_handler.read_file()
        mock_print.assert_called_with(self.txt_text_to_write)

    @patch('builtins.print')
    def test_read_empty_file(self, mock_print):
        self.txt_empty.read_file()
        mock_print.assert_called_with(print_empty_file)

    @patch('builtins.print')
    def test_csv_write_to_file(self, mock_print):
        self.csv_file_handler.write_to_file(self.csv_text_to_write)

        file = open(self.csv_file, 'r')
        text = file.read()

        self.assertEqual(text, self.csv_result_text)

        file.close()
        os.remove(self.csv_file)

        mock_print.assert_called_with(print_success_write)

    @patch('core.file_handler_abc.default_write_to_file')
    def test_txt_write_to_file(self, mock_default_write_to_file):
        self.txt_file_handler.write_to_file(self.txt_text_to_write)
        self.assertTrue(mock_default_write_to_file.called)

    @patch('core.file_handler_abc.default_write_to_file')
    def test_doc_write_to_file(self, mock_default_write_to_file):
        self.doc_file_handler.write_to_file(self.txt_text_to_write)
        self.assertTrue(mock_default_write_to_file.called)


if __name__ == "__main__":
    unittest.main()
