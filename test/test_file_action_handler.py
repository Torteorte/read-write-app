import unittest
from core.file_action_handler import FileActionHandler
from core.file_Handler_abc import CSVFileHandler, TXTFileHandler, DOCFileHandler


class TestFileActionHandler(unittest.TestCase):
    test_txt = 'test.txt'
    test_csv = 'test.csv'
    test_doc = 'test.doc'

    def setUp(self):
        self.FileActionHandler = FileActionHandler()

    def test_get_file_handler_by_extension(self):
        self.assertIsInstance(self.FileActionHandler.get_file_handler_by_extension(self.test_txt),
                              type(TXTFileHandler(self.test_txt)))

        self.assertIsInstance(self.FileActionHandler.get_file_handler_by_extension(self.test_csv),
                              type(CSVFileHandler(self.test_csv)))

        self.assertIsInstance(self.FileActionHandler.get_file_handler_by_extension(self.test_doc),
                              type(DOCFileHandler(self.test_doc)))

        self.assertNotIsInstance(self.FileActionHandler.get_file_handler_by_extension(self.test_txt),
                                 type(DOCFileHandler(self.test_txt)))


if __name__ == '__main__':
    unittest.main()
