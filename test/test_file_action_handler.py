import unittest
from unittest.mock import patch

from core.file_action_handler import FileActionHandler
from core.file_Handler_abc import CSVFileHandler, TXTFileHandler, DOCFileHandler
from constants.constants import read_mode, write_mode, test_txt_extension, test_csv_extension, test_doc_extension


class TestFileActionHandler(unittest.TestCase):
    test_txt_extension = test_txt_extension
    test_csv_extension = test_csv_extension
    test_doc_extension = test_doc_extension

    def setUp(self):
        self.fileActionHandler = FileActionHandler()

    def test_get_file_handler_by_extension(self):
        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_txt_extension),
                              type(TXTFileHandler(self.test_txt_extension)))

        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_csv_extension),
                              type(CSVFileHandler(self.test_csv_extension)))

        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_doc_extension),
                              type(DOCFileHandler(self.test_doc_extension)))

        self.assertNotIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_txt_extension),
                                 type(DOCFileHandler(self.test_txt_extension)))

    def test_do_action_read(self):
        self.fileActionHandler.get_file_handler_by_extension(self.test_csv_extension)

        patcher = patch.object(CSVFileHandler, 'read_file')
        patched = patcher.start()

        self.fileActionHandler.do_action(read_mode)
        assert patched.call_count == 1

    def test_do_action_write(self):
        patcher = patch.object(TXTFileHandler, 'write_to_file')
        patched = patcher.start()

        self.fileActionHandler.get_file_handler_by_extension(self.test_txt_extension)
        self.fileActionHandler.do_action(write_mode)

        assert patched.call_count == 1


if __name__ == '__main__':
    unittest.main()
