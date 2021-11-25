import unittest
from core.file_path_handler import FilePathHandler


class TestFileHandler(unittest.TestCase):
    test_txt = 'test/some_test.txt'
    test_csv = 'mythic.csv'
    test_jp = 'test.木'

    def setUp(self):
        self.FilePathHandler = FilePathHandler('', '')

    def test_check_file_status(self):
        self.assertIsNone(self.FilePathHandler.check_file_status(self.test_txt))
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_status(self.test_csv)
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_status(self.test_jp)

    def test_check_file_extension(self):
        self.assertIsNone(self.FilePathHandler.check_file_extension(self.test_txt))
        self.assertIsNone(self.FilePathHandler.check_file_extension(self.test_csv))
        with self.assertRaises(TypeError):
            self.FilePathHandler.check_file_extension(self.test_jp)

    def test_check_file(self):
        self.assertEqual(self.FilePathHandler.check_file(self.test_txt), self.test_txt)


if __name__ == '__main__':
    unittest.main()
