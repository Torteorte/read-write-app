import unittest
from core.FileActionHandler import FileActionHandler
from core.FileHandlerABS import CSVFileHandler, TXTFileHandler, DOCFileHandler


class TestFileActionHandler(unittest.TestCase):
    def setUp(self):
        self.FileActionHandler = FileActionHandler()

    def test_get_file_handler_by_extension(self):
        text_txt = 'test.txt'
        text_csv = 'test.csv'
        text_doc = 'test.doc'

        self.assertEqual(self.FileActionHandler.get_file_handler_by_extension(text_txt).__class__,
                         TXTFileHandler(text_txt).__class__)

        self.assertEqual(self.FileActionHandler.get_file_handler_by_extension(text_csv).__class__,
                         CSVFileHandler(text_csv).__class__)

        self.assertEqual(self.FileActionHandler.get_file_handler_by_extension(text_doc).__class__,
                         DOCFileHandler(text_doc).__class__)

        self.assertNotEqual(self.FileActionHandler.get_file_handler_by_extension(text_txt).__class__,
                            DOCFileHandler(text_txt).__class__)


if __name__ == '__main__':
    unittest.main()
