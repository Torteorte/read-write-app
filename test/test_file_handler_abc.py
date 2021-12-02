import os
import unittest
from unittest.mock import patch

from core.file_handler import FileHandlerABC, CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import print_empty_file, print_success_write
from test.constants.constatns import test_csv_file_name, test_txt_file_name, test_doc_file_name, test_txt_file_empty, \
    test_text_to_write, csv_test_text_to_write, csv_result_text, builtins_print, path_of_default_write_to_file


class TestFileHandlerABC(unittest.TestCase):

    @patch("core.file_handler.FileHandlerABC.__abstractmethods__", set())
    def test_abstract_class(self):
        file_handler_abc = FileHandlerABC('')
        self.assertIsNone(file_handler_abc.write_to_file(''))

    @patch(builtins_print)
    def test_read_empty_file(self, mock_print):
        txt_empty = TXTFileHandler(test_txt_file_empty)
        txt_empty.read_file()

        mock_print.assert_called_with(print_empty_file)

    @patch(builtins_print)
    def test_csv_write_to_file(self, mock_print):
        csv_file_handler = CSVFileHandler(test_csv_file_name)
        csv_file_handler.write_to_file(csv_test_text_to_write)

        file = open(test_csv_file_name, 'r')

        self.assertEqual(file.read(), csv_result_text)

        file.close()
        os.remove(test_csv_file_name)

        mock_print.assert_called_with(print_success_write)

    @patch(path_of_default_write_to_file)
    def test_txt_write_to_file(self, mock_default_write_to_file):
        txt_file_handler = TXTFileHandler(test_txt_file_name)
        txt_file_handler.write_to_file(test_text_to_write)

        self.assertTrue(mock_default_write_to_file.called)

    @patch(path_of_default_write_to_file)
    def test_doc_write_to_file(self, mock_default_write_to_file):
        doc_file_handler = DOCFileHandler(test_doc_file_name)
        doc_file_handler.write_to_file(test_text_to_write)

        self.assertTrue(mock_default_write_to_file.called)


if __name__ == "__main__":
    unittest.main()
