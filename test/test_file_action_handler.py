import unittest
from unittest.mock import patch

from core.file_action_handler import FileActionHandler
from core.file_Handler_abc import CSVFileHandler, TXTFileHandler, DOCFileHandler


class TestFileActionHandler(unittest.TestCase):
    test_txt = 'test.txt'
    test_csv = 'test.csv'
    test_doc = 'test.doc'

    def setUp(self):
        self.fileActionHandler = FileActionHandler()

    def test_get_file_handler_by_extension(self):
        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_txt),
                              type(TXTFileHandler(self.test_txt)))

        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_csv),
                              type(CSVFileHandler(self.test_csv)))

        self.assertIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_doc),
                              type(DOCFileHandler(self.test_doc)))

        self.assertNotIsInstance(self.fileActionHandler.get_file_handler_by_extension(self.test_txt),
                                 type(DOCFileHandler(self.test_txt)))

    def test_do_action_read(self):
        self.fileActionHandler.get_file_handler_by_extension(self.test_csv)

        patcher = patch.object(CSVFileHandler, 'read_file')
        patched = patcher.start()

        self.fileActionHandler.do_action('read')
        assert patched.call_count == 1

    def test_do_action_write(self):
        self.fileActionHandler.get_file_handler_by_extension(self.test_txt)

        patcher = patch.object(TXTFileHandler, 'write_to_file')
        patched = patcher.start()

        self.fileActionHandler.do_action('write')
        assert patched.call_count == 1


if __name__ == '__main__':
    unittest.main()