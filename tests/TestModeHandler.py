import unittest
from core.ModeHandler import ModeHandler


class TestModeHandler(unittest.TestCase):
    def setUp(self):
        self.modeHandler = ModeHandler()

    def test_check_mode(self):
        self.assertEqual(self.modeHandler.check_mode('1'), 'read')
        self.assertEqual(self.modeHandler.check_mode('read'), 'read')
        self.assertEqual(self.modeHandler.check_mode('2'), 'write')
        self.assertEqual(self.modeHandler.check_mode('write'), 'write')


if __name__ == "__main__":
    unittest.main()
