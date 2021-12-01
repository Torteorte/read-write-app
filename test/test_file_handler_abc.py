import os
import unittest
from unittest.mock import patch

from core.file_handler_abc import FileHandlerABC, CSVFileHandler, TXTFileHandler, DOCFileHandler, FileHandler
from constants.constants import print_empty_file, print_success_write

from test.constants.constatns import test_csv_file_name, test_txt_file_name, test_doc_file_name, test_txt_file_empty, \
    test_text_to_write, csv_test_text_to_write, csv_result_text, test_txt_file_name_for_read


class TestFileHandlerABC(unittest.TestCase):

    @patch("core.file_handler_abc.FileHandlerABC.__abstractmethods__", set())
    def test_abstract_class(self):
        file_handler_abc = FileHandlerABC()
        with self.assertRaises(NotImplementedError):
            file_handler_abc.read_file()

        with self.assertRaises(NotImplementedError):
            file_handler_abc.write_to_file('')

    @patch('builtins.print')
    def test_read_file(self, mock_print):
        file_handler = FileHandler(test_txt_file_name_for_read)
        file_handler.read_file()

        mock_print.assert_called_with(test_text_to_write)

    @patch('builtins.print')
    def test_read_empty_file(self, mock_print):
        txt_empty = TXTFileHandler(test_txt_file_empty)
        txt_empty.read_file()

        mock_print.assert_called_with(print_empty_file)

    @patch('builtins.print')
    def test_csv_write_to_file(self, mock_print):
        csv_file_handler = CSVFileHandler(test_csv_file_name)
        csv_file_handler.write_to_file(csv_test_text_to_write)

        file = open(test_csv_file_name, 'r')

        self.assertEqual(file.read(), csv_result_text)

        file.close()
        os.remove(test_csv_file_name)

        mock_print.assert_called_with(print_success_write)

    @patch('core.file_handler_abc.default_write_to_file')
    def test_txt_write_to_file(self, mock_default_write_to_file):
        txt_file_handler = TXTFileHandler(test_txt_file_name)
        txt_file_handler.write_to_file(test_text_to_write)

        self.assertTrue(mock_default_write_to_file.called)

    @patch('core.file_handler_abc.default_write_to_file')
    def test_doc_write_to_file(self, mock_default_write_to_file):
        doc_file_handler = DOCFileHandler(test_doc_file_name)
        doc_file_handler.write_to_file(test_text_to_write)

        self.assertTrue(mock_default_write_to_file.called)


if __name__ == "__main__":
    unittest.main()
