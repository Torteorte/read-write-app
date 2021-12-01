import unittest
from unittest.mock import patch

from core.file_action_handler import FileActionHandler
from core.file_handler import CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import read_mode, write_mode
from test.constants.constatns import test_txt_extension, test_csv_extension, test_doc_extension, path_of_csv_read_file, \
    path_of_csv_write_to_file


class TestFileActionHandler(unittest.TestCase):
    def setUp(self):
        self.fileActionHandler = FileActionHandler()

    def test_get_file_handler_by_extension_by_txt(self):
        self.assertIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_txt_extension),
            type(TXTFileHandler(test_txt_extension))
        )
        self.assertNotIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_csv_extension),
            type(TXTFileHandler(test_csv_extension))
        )

    def test_get_file_handler_by_extension_by_csv(self):
        self.assertIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_csv_extension),
            type(CSVFileHandler(test_csv_extension))
        )
        self.assertNotIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_txt_extension),
            type(CSVFileHandler(test_txt_extension))
        )

    def test_get_file_handler_by_extension_by_doc(self):
        self.assertIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_doc_extension),
            type(DOCFileHandler(test_doc_extension))
        )
        self.assertNotIsInstance(
            self.fileActionHandler.get_file_handler_by_extension(test_txt_extension),
            type(DOCFileHandler(test_txt_extension))
        )

    @patch(path_of_csv_read_file)
    def test_do_action_read(self, mock_read_file):
        self.fileActionHandler.get_file_handler_by_extension(test_csv_extension)
        self.fileActionHandler.do_action(read_mode)

        self.assertTrue(mock_read_file.called)

    @patch('core.file_handler.TXTFileHandler.write_to_file')
    def test_do_action_write(self, mock_write_to_file):
        self.fileActionHandler.get_file_handler_by_extension(test_txt_extension)
        self.fileActionHandler.do_action(write_mode)

        self.assertTrue(mock_write_to_file.called)


if __name__ == '__main__':
    unittest.main()
