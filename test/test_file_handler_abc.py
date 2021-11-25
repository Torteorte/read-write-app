import unittest
import os
from core.file_Handler_abc import CSVFileHandler
from constants.constants import csv_test_text_to_write, test_csv_file_name, result_text


class TestCSVFileHandler(unittest.TestCase):
    test_file_name = test_csv_file_name
    text_to_write = csv_test_text_to_write
    result_text = result_text

    def setUp(self):
        self.CSVFileHandler = CSVFileHandler(self.test_file_name)

    def test_read_file(self):
        self.CSVFileHandler.write_to_file(self.text_to_write)

        file = open(self.test_file_name, 'r')
        text = file.read()

        self.assertEqual(text, self.result_text)

        file.close()

    def tearDown(self):
        os.remove(self.test_file_name)


if __name__ == "__main__":
    unittest.main()
