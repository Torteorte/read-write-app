import os
import unittest

from core.file_Handler_abc import CSVFileHandler, TXTFileHandler
from constants.constants import csv_test_text_to_write, test_csv_file_name, result_text, test_text_to_write, \
    test_txt_file_name


class TestCSVFileHandler(unittest.TestCase):
    test_file_name = test_csv_file_name
    text_to_write = csv_test_text_to_write
    result_text = result_text
    test_text_to_write = test_text_to_write
    test_txt_file_name = test_txt_file_name

    def setUp(self):
        self.CSVFileHandler = CSVFileHandler(self.test_file_name)
        self.TXTFileHandler = TXTFileHandler(self.test_txt_file_name)

    def test_read_file(self):
        file = open(self.test_txt_file_name, 'r')
        text = file.read()

        self.assertEqual(text, self.test_text_to_write)

        file.close()

    def test_csv_write_to_file(self):
        self.CSVFileHandler.write_to_file(self.text_to_write)

        file = open(self.test_file_name, 'r')
        text = file.read()

        self.assertEqual(text, self.result_text)

        file.close()
        os.remove(self.test_file_name)


if __name__ == "__main__":
    unittest.main()
